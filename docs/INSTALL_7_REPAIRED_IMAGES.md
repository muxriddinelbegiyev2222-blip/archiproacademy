# Yetti shikastlangan ARCHIPRO UZ dars tasvirini tiklash

Holat: yangi yetti JPEG tasvir **alohida ZIP paketda** tayyorlangan. GitHub manba repozitoriysiga binar JPEG fayllar **hali yuborilmagan**; rasmlar allaqachon yuklangan deb hisoblamang.

1. `archipro_7_repaired_images.zip` paketini ChatGPT suhbatidagi yuklab olish havolasidan kompyuterga oling.
2. GitHub repozitoriysining **so‘nggi `main`** versiyasini kompyuterga yuklang yoki `git pull origin main` bajaring.
3. ZIP faylni repozitoriy ildiziga (README.md turgan joyga) qo‘ying. **Arxivni ochish talab qilinmaydi.**
4. Terminalni shu katalogda ochib bajaring:
   ```powershell
   python tools/install_seven_repaired_media.py archipro_7_repaired_images.zip
   python tools/verify_compact_media.py --require-complete
   python app/tools/project_audit.py
   python app/tools/database_audit.py
   python app/tools/runtime_smoke_test.py
   python app/tools/customer_features_smoke_test.py
   python app/tools/ui_navigation_smoke_test.py
   python app/tools/learning_flow_smoke_test.py
   python app/tools/release_regression_test.py
   ```
5. Faqat hammasi **PASS** bo‘lsa o‘zgarishlarni `git add app/courses/visual_assets app/courses/visual_catalog.py docs/MEDIA_COMPRESSION_2026_10_09.json`, so‘ng `git commit -m "Restore seven damaged lesson images"` va `git push origin main` orqali yuboring. Kerak bo‘lsa `git status` orqali o‘zgargan boshqa reyestr fayllarini ham ko‘rib chiqing.
6. `archipro_7_repaired_images.zip` va shaxsiy zaxira nusxalarini commitga qo‘shmang.

Skript haqiqiy SVG fayllarning SHA-256 imzosini va yangi rasmlar hajmi/SHAsini tekshiradi; koddagi va JSON reyestrlardagi eski nomlarni almashtiradi; yangi fayllar va hisobotni tekshirib, xatolik bo‘lsa dastlabki holatga qaytaradi. Asl eskizlar oxirgi tekshiruvdan keyin o‘chiriladi. Skriptning birinchi muvaffaqiyatli ishlashi 271/278 hisobini 278/278 ga aylantiradi.

Muhim: SHNQ/QMQ bo‘yicha normativ ekspertiza bu vizual tiklash ishining doirasiga kirmaydi. Windows CI runnerlariga kvota/billing cheklovi qo‘yilgan bo‘lsa, Actions natijasi muvaffaqiyatli ko‘rinmaguncha reliz tayyor deb e’lon qilinmasin.
