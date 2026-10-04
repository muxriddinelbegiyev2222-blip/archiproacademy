# ARCHIPRO UZ

ARCHIPRO UZ — Windows uchun to'liq offline arxitektura va Archicad o'quv platformasi.

## Maqsad

Arxitekturani mutlaqo 0 dan boshlab O'zbekiston sharoitidagi
1 va 2 qavatli yakka tartibdagi turar joylarni professional
darajada loyihalashgacha bosqichma-bosqich o'rgatish.

## O'quv tizimi

- 16 Level: LEVEL 00–15
- 137 modul
- 680 dars
- 2041 mini-test savoli
- Level yakuniy imtihonlari
- Progress, XP va mastery gate
- PRO ketma-ket o'qish rejimi
- OWNER uchun alohida MASTER test rejimi

## Asosiy yo'nalishlar

- Arxitektura asoslari
- Archicad
- 1 va 2 qavatli turar joylar
- Ergonomika
- Genplan
- Fasad va kesim
- Qurilish konstruksiyalari
- SHNQ va normativlar
- BIM
- Ishchi loyiha
- Amaliy mashqlar
- Test va imtihonlar
- Portfolio / PRO Final

## Mijoz qulayliklari

- Bosh sahifadan bir bosishda o'qishni davom ettirish
- Yaqinda ko'rilgan darslar
- Global dars qidiruvi
- Dars bookmarklari
- Har bir dars uchun shaxsiy eslatmalar va autosave
- Kutubxonada faqat bookmark yoki eslatmali darslarni ko'rish
- Mini-testdan keyin Keyingi dars tugmasi
- Ctrl+K global qidiruv
- Esc orqaga qaytish
- Ctrl+Right keyingi dars
- Offline terminlar lug'ati
- Offline yordam markazi
- Progress / test / imtihon / bookmark / eslatma backup va restore

## Offline litsenziyalash

- Device ID asosidagi aktivatsiya
- Ed25519 imzolangan .archiprolic
- Mijoz uchun PRO license
- Dastur egasi uchun alohida MASTER license
- Private key klient dasturiga kiritilmaydi

## Platforma

Windows Desktop

## Versiya

ARCHIPRO UZ v1.0.4 — Release Candidate


## Release sifat nazorati

Release build quyidagi tekshiruvlardan o'tmasdan yaratilmaydi:

- Project Audit
- Database Audit
- Runtime Smoke Test
- Customer Features Smoke Test
- UI Navigation Smoke Test
- Learning Flow Smoke Test

UI Navigation Smoke Test real `OCHISH` tugmasini bosib,
Level -> Lesson -> Orqaga navigatsiya zanjirini tekshiradi.
Learning Flow Smoke Test esa mini-test, progress, keyingi dars
qulfi, real score va attempt hisobini tekshiradi.

## v1.0.4 tuzatishlar

- Dars, mini-test, imtihon va Level qaytish tugmalari Qt `checked` qiymatini sahifa manziliga aralashtirmaydi.
- LEVEL 00 / MODULE 02–03 matni va testlari to'g'ri manbadan yuklanadi.
- Darsdan tez chiqish va oynani yopishda pending eslatma saqlanadi.
- Eski kechiktirilgan tozalash qayta ochilgan yangi darsni o'chirmaydi.
- Test va imtihon bir tekshirish uchun bitta urinish yozadi.
- Sana vaqt zonasi bilan yozilgan litsenziyalar tekshiriladi.
- BUILD_EXE dinamik kurs modullarini yig'adi va to'liq auditdan o'tishni talab qiladi.

`AUDIT_ARCHIPRO.bat` barcha 7 auditni bajaradi. Batafsil natijalar
`audit_logs` papkasida saqlanadi. `python app/tools/full_audit.py` ham ishlaydi.
Yangi Release Regression Test 680 ta dars sahifasi, 16 imtihon,
barcha menyular, eslatmalar, tez navigatsiya, litsenziya imzosi,
backup rollback va PRO kursining to'liq o'quv jarayonini tekshiradi.

Windows EXE va installer shu manba koddan Windowsda yig'iladi.
Linuxdagi Qt offscreen tekshiruv Windows installer/real ekran tekshiruvini almashtirmaydi.

## v1.0.5: dars kontenti va Windows EXE tekshiruvi

Dars kontenti yuklanmasa, qisqa izoh to'liq dars o'rnida takrorlanmaydi.
Sahifa aniq xabar beradi va kontentsiz mini-testni boshlashni bloklaydi.
Birinchi dars 7 ta mazmunli blokdan iborat.

BUILD_EXE va BUILD_RELEASE endi yig'ilgan EXE ichidagi barcha 680 dars va
680 mini-testni tekshiradi. Kontent modullari yetishmasa build muvaffaqiyatli
hisoblanmaydi. Windows CI ham EXE yig'adi, uni tekshiradi va muvaffaqiyatli
natijani ARCHIPRO_UZ_Client_1.0.5 artifact sifatida saqlaydi.

GitHubdagi kodni yangilash oldin yig'ilgan EXEni almashtirmaydi. Yangilangan
EXEni o'rnating yoki BUILD_RELEASE.bat orqali qayta yig'ing.

EXE build barcha mahalliy courses, licensing va ui modullarini fayllardan
aniq ro'yxat qilib yig'adi. Bu dinamik importlar build vaqtida o'tib ketishiga
yo'l qo'ymaydi. Build kirish nuqtasi: app/tools/build_client.py.
