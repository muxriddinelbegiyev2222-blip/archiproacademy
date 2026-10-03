@echo off
setlocal

title ARCHIPRO UZ - LICENSE KEY GENERATOR

cd /d "%~dp0"

echo.
echo ============================================================
echo          ARCHIPRO UZ - LICENSE KEY GENERATOR
echo ============================================================
echo.

where python >nul 2>&1

if errorlevel 1 (
    echo [ERROR] Python topilmadi.
    pause
    exit /b 1
)

echo [OK] Python topildi.

echo.

python -c "import cryptography" >nul 2>&1

if errorlevel 1 (
    echo [INFO] cryptography kutubxonasi o'rnatilmoqda...
    echo.

    python -m pip install cryptography

    if errorlevel 1 (
        echo.
        echo [ERROR] cryptography o'rnatilmadi.
        pause
        exit /b 1
    )
)

echo [OK] cryptography tayyor.

echo.
echo License key yaratilmoqda...
echo.

python "app\licensing\keygen.py"

echo.
echo ============================================================
echo TAYYOR
echo ============================================================
echo.
echo EKRANDAGI PUBLIC KEYNI CHATGPT'GA YUBORING.
echo.
echo PRIVATE KEYNI YUBORMANG.
echo.
echo Private key:
echo %%LOCALAPPDATA%%\ARCHIPRO_UZ_ADMIN\keys\archipro_private.key
echo.

pause
