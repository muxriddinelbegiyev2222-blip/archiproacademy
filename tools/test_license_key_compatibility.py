"""Security regressions for ARCHIPRO UZ signed-license compatibility.

No real private keys or customer license files are needed. This validates that
only correctly signed licenses from the current or legacy signing key are
accepted, while device binding, expiry, and tamper protection remain active.
"""
import base64
import hashlib
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "app"))

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from licensing import license_service as s


class TrustedPublicKeyTests(unittest.TestCase):
    def test_real_key_fingerprints_match_diagnosis(self):
        primary = base64.b64decode(s.PUBLIC_KEY_B64, validate=True)
        legacy = base64.b64decode(s.LEGACY_PUBLIC_KEY_B64, validate=True)
        self.assertEqual(len(primary), 32)
        self.assertEqual(len(legacy), 32)
        self.assertEqual(hashlib.sha256(primary).hexdigest().upper()[:16],
                         "F7AFC1C00E6D7DDE")
        self.assertEqual(hashlib.sha256(legacy).hexdigest().upper()[:16],
                         "2BCB7109E86D65DD")
        self.assertNotEqual(primary, legacy)

    def test_signatures_device_lock_and_rejection(self):
        # Two independent signing keys simulate OWNER current and legacy keys.
        current_private = Ed25519PrivateKey.generate()
        legacy_private = Ed25519PrivateKey.generate()
        attacker_private = Ed25519PrivateKey.generate()
        payload = {
            "device_id": "ARCHIPRO-1111-2222-3333-4444-5555-6666",
            "username": "example_user",
            "password_hash": "unit-test-hash",
            "password_salt": "unit-test-salt",
            "license_type": "PRO",
            "expires_at": None,
        }

        def signed(key, attributes=None):
            body = dict(payload, **(attributes or {}))
            return {
                "product": s.PRODUCT_NAME,
                "version": s.LICENSE_VERSION,
                "payload": body,
                "signature": base64.b64encode(
                    key.sign(s._canonical_payload(body))
                ).decode("ascii"),
            }

        patches = (
            patch.object(s, "_load_public_key", return_value=current_private.public_key()),
            patch.object(s, "_load_legacy_public_key", return_value=legacy_private.public_key()),
            patch.object(s, "get_device_id", return_value=payload["device_id"]),
        )
        with patches[0], patches[1], patches[2]:
            self.assertTrue(s.verify_license_data(signed(current_private))["valid"])
            self.assertTrue(s.verify_license_data(signed(legacy_private))["valid"])
            invalid = s.verify_license_data(signed(attacker_private))
            self.assertFalse(invalid["valid"])
            self.assertIn("imzosi", invalid["message"])
            changed = signed(current_private)
            changed["payload"]["license_type"] = "MASTER"
            self.assertFalse(s.verify_license_data(changed)["valid"])
            broken_signature = signed(current_private)
            broken_signature["signature"] = "invalid-base64!"
            self.assertFalse(s.verify_license_data(broken_signature)["valid"])
            with patch.object(s, "get_device_id", return_value="ARCHIPRO-OTHER-DEVICE"):
                invalid = s.verify_license_data(signed(current_private))
                self.assertFalse(invalid["valid"])
                self.assertIn("boshqa kompyuter", invalid["message"])

            wrong_product = signed(current_private)
            wrong_product["product"] = "OTHER"
            self.assertFalse(s.verify_license_data(wrong_product)["valid"])
            wrong_version = signed(current_private)
            wrong_version["version"] = 999
            self.assertFalse(s.verify_license_data(wrong_version)["valid"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
