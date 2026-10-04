# ARCHIPRO UZ 1.0.6 — darslarning amaliy qismini yangilash

680 darsning mavjud o‘quv matni va 137 modul tuzilishi saqlandi. Har darsga o‘quv holati, mavzuga mos topshiriq, namunaviy xulosa, mustaqil mashq va baholash rubrikasi qo‘shildi. 137 holat va 680 topshiriq alohida yozilgan; bir modul darslari bitta holatning turli tomonlarini tekshiradi.

678 darsdagi 2035 savol mavzuga mos holat va topshiriqlar bilan yangilandi. Oldingi ikki to‘liq to‘rt variantli test saqlandi. Jami 2041 savolning har birida to‘rtta variant va bitta to‘g‘ri javob bor. Savol kodlari va dars IDlari saqlandi. To‘liq bir xil test to‘plamlari yo‘q. Noto‘g‘ri variantlarda modulga xos xato va tekshirilmagan xulosalar ishlatiladi. Bu testlar o‘qilgan tushunchani tekshiradi; amaliy loyiha sifatini avtomatik baholamaydi.

Archicad bo‘yicha matnlarda 28 INT versiyasi ko‘rsatilgan. Rasmiy Graphisoft yordam havolalari qo‘shilgan. Normativ va konstruktsiya mashqlarida o‘quv raqamlari haqiqiy loyiha talabi yoki hisoblangan kesim bilan tenglashtirilmaydi. Talabni tekshirishda asl hujjat doirasi, amaldagi tahriri, bandi va mutaxassis tasdig‘i qayd etiladi. Matn oflayn ishlaydi; tashqi manba havolasini ochish uchun internet kerak.

## Yangilash

Yangi kod mavjud EXEni avtomatik almashtirmaydi. Windowsda `BUILD_RELEASE.bat` orqali yangi mijoz dasturi va installer yig‘iladi. Yig‘ilgan EXEning ichidagi barcha 680 dars, ish daftarlari va testlar alohida tekshiriladi. Ilova yangi content versiyasini aniqlab, testlarni yangilaydi; foydalanuvchi progressini va tarixiy ballarni qaytadan hisoblamaydi.

CI main va `curriculum-quality-v1.0.6` tarmog‘ida ishlaydi. Artifact yuklash GitHub saqlash kvotasiga bog‘liq; artifact yuklanmasligi EXE yig‘ish yoki tekshirish natijasini almashtirmaydi.

## Tekshiruv va uning chegarasi

Release regression mavjud o‘quv matni o‘chmaganini, barcha darslar qamrab olinganini, lazy/full registry natijalari mosligini va savol kodlari saqlanganini tekshiradi. Eski testlarni bazaga joylab, eski content versiyasidan yangi versiyaga ko‘tarishda foydalanuvchilar, progress, eslatmalar, xatcho‘plar, quiz va imtihon urinishlari o‘zgarmasligi tekshiriladi. To‘liq Qt o‘quv yo‘li 680 dars va 16 imtihondan o‘tadi.

Bu yangilash o‘quv materialini amaliy va tushunarli qiladi. Strukturaviy testlar barcha arxitektura jumlalarining ekspert tasdig‘i yoki 100% xatosizlik sertifikati emas. Yangilash video darslar, haqiqiy Archicad ekran yozuvlari yoki tayyor PLN loyiha fayllarini qo‘shmaydi. Mustaqil mashqni o‘quvchi yoki ustoz rubrika bilan baholaydi. Qurilishga oid aniq hisob va amaldagi normativ moslik tegishli mutaxassislar bilan tekshiriladi.
