"""Long-form demonstrations for foundational tasks that need a complete worked chain."""
EXAMPLES = {
'L00_M02_001': '''
<h3>Planda xonalarni qanday joylashtirishni boshlaymiz?</h3>
<p>Plan binoning yuqoridan o‘qiladigan gorizontal ko‘rinishi bo‘lib, xonalar va elementlarning o‘zaro joylashuvini tushuntiradi.
Devor, eshik va derazani sanab chiqish planni ishlashga o‘rgatmaydi. Quyidagi misolda qarorlar qanday hosil bo‘lishini ko‘ramiz.</p>
<p><b>Shart:</b> to‘rt kishilik oila, ikki yotoqxona, mehmonxona, oshxona–ovqatlanish, kirish va sanuzel.
Avval xonalar aloqasini sinaymiz. Quyidagi 10×8 m to‘rtburchak devor qalinligisiz <b>o‘quv zonalash sxemasi</b>:
qurilishga tayyor plan yoki talabga mosligi tasdiqlangan loyiha emas.</p>
<ol>
<li><b>Vazifani aniqlang.</b> Ota-ona va bolalar tinch uxlaydi, mehmon kirishdan umumiy xonaga boradi,
ovqat oshxonada tayyorlanadi. Har xonaga kim va nima uchun kirishini yozing.</li>
<li><b>Aloqani tuzing.</b> Kirish→umumiy yo‘lak→mehmonxona. Oshxona→ovqatlanish yaqin.
Yo‘lak→ikki yotoqxona va sanuzel. Mehmon yotoqxona orqali o‘tmaydi.</li>
<li><b>Kontur ichida guruhlang.</b> Yuqoridagi 4 m chuqur tasma tinch xonalar,
uning pastida 1.2 m chuqur yo‘lak, qolgan 2.8 m tasma umumiy xona va kirish bo‘lsin.
4+1.2+2.8=8 m. Gorizontal bo‘linish 4+4+2=10 m.
Bu qiymatlar geometriyani ko‘rsatadi; yo‘lak va xonalarning haqiqiy talablari alohida tekshiriladi.</li>
</ol>
<table border="1" cellspacing="0" cellpadding="8" width="100%">
<tr><td bgcolor="#E7F0E8">Yotoqxona 1<br>4×4 m = 16 m²</td><td bgcolor="#E7F0E8">Yotoqxona 2<br>4×4 m = 16 m²</td><td>Sanuzel<br>2×4 m = 8 m²</td></tr>
<tr><td colspan="3" bgcolor="#F4E9D7">Umumiy yo‘lak — 10×1.2 m = 12 m². Har xonaga alohida kirish shu tasmadan.</td></tr>
<tr><td>Mehmonxona<br>4×2.8 m = 11.2 m²</td><td>Oshxona–ovqatlanish<br>4×2.8 m = 11.2 m²</td><td bgcolor="#F4E9D7">Kirish<br>2×2.8 m = 5.6 m²</td></tr>
</table>
<p><b>Sxemani o‘qing:</b> tashqi kirish pastki o‘ng blokda. Har xona yo‘lakka bog‘lanadi.
Jadval eshik, deraza yoki konstruksiyaning tayyor chizmasi emas — faqat aloqani tushuntiradi.</p>
<ol start="4">
<li><b>Mebel bilan sinang.</b> Yotoqxonaga 2×1.6 m o‘quv krovat va 0.6 m chuqur shkafni haqiqiy masshtabda chizing.
Eshikdan krovat va shkafgacha yo‘l qoldiring. Mebel korpusi bilan uning oldida foydalaniladigan joyni ajrating.
Mehmonxonaga o‘tirish guruhini, oshxonaga jihoz va stul surilish zonalarini qo‘ying.
Sxemadagi 11.2 m² xona kerakli faoliyatga yetmasa, guruhlarning o‘lchamini qayta taqsimlang.</li>
<li><b>Eshik va derazalarni tanlang.</b> Eshikni mebel ortiga qo‘ymang. Ochilish yoylarini chizing,
yonma-yon eshiklar to‘qnashishini tekshiring. Derazani tashqi devorga xona ehtiyoji, quyosh va qo‘shni bilan aloqadan kelib chiqib joylang.
Deraza o‘rni fasadga ham chiqishi kerak.</li>
<li><b>Devorni kiriting.</b> Zonalash to‘g‘ri ishlagach devor turi va qalinligini loyiha sharti bilan belgilang.
Devorlar maydon egallaydi: yuqoridagi 80 m² sof taqsimot qalinlik qo‘shilganda avtomatik saqlanmaydi.
Tashqi kontur qat’iy bo‘lsa ichki maydon kamayadi; ichki o‘lcham qat’iy bo‘lsa tashqi kontur kattalashadi.</li>
<li><b>Yozuv va o‘lcham qo‘ying.</b> Har xonaning nomi va qayta hisoblangan sof maydonini yozing.
Ichki o‘lchamni devor yuzalari, tashqi o‘lchamni tashqi kontur bo‘yicha ko‘rsating. Birlikni yozing.
Kesim chizig‘i, kerakli belgilar va sathlarni hujjat maqsadiga mos kiriting.</li>
<li><b>Foydalanib tekshiring.</b> Mehmon, bola va ovqat olib ketayotgan odamning yo‘lini uch alohida chiziq bilan chizing.
Eshiklar ochiq holatda yo‘l ishlaydimi? Sanuzelga yotoqxonadan o‘tish kerak emasmi?
Oshxonadagi odam kirish oqimi bilan to‘qnashmaydimi? Muammo bo‘lsa avval aloqa va mebelni, keyin devorlarni tuzating.</li>
</ol>
<p><b>Hisobni tekshirish:</b> 16+16+8+12+11.2+11.2+5.6=80 m², 10×8=80 m².
Bu faqat devorsiz tasmalarning yig‘indisi. Chizma talabga mosligi va foydali maydon haqiqiy devorlar, jihozlar,
foydalanish hamda tegishli loyiha talablari bilan qayta tekshiriladi.</p>
<p><b>Noto‘g‘ri variant:</b> yotoqxona 1 eshigi faqat yotoqxona 2ga ochildi.
Birinchi xonaga kirish uchun boshqa odamning shaxsiy joyidan o‘tiladi.
<b>Tuzatish:</b> ikkala xonaga umumiy yo‘lakdan alohida kirish tashkil qiling; eshik yoylarini mebel bilan qayta sinang.</p>
<p><b>Mustaqil mashq va yechim:</b> oshxonadan hovliga eshik kerak bo‘ldi.
Pastki tashqi devorda chiqish variantini belgilang, jihoz va diningni uning yo‘lidan ajrating,
fasad ochilishini yangilang, genplanda stol/hovligacha yo‘lni chizing.
To‘g‘ri javob faqat “eshik qo‘shildi” emas: barcha aloqalar va foydalanish yo‘li tekshirilgan.</p>
''',
'L05_M03_001': '''
<h3>4000 mm devorni qiymat bilan yaratish</h3>
<p>Floor Plan oynasida o‘quv nusxa bilan ishlang. Working Unitsni tekshiring: bu mashq millimetrda.
ToolBoxdan Wallni tanlang, asbob sozlamalarini oching. 200 mm qalinlik, 3000 mm o‘quv balandligi va kerakli Home Storyni tekshiring.
Reference line tanlangan ichki yuza bo‘ylab bo‘lsin. Bu qiymatlar konstruktiv yoki normativ tavsiya emas.</p>
<ol><li>Boshlanish nuqtasini bosing. Kursorni kerakli yo‘nalishga olib boring.</li>
<li>Trackerda Distance maydonini tanlang. Tab bilan kerakli maydonga o‘tish yoki maydonni bosish mumkin.
4000 qiymatini kiriting; Angle maydonini tanlangan yo‘nalishga tekshiring.</li>
<li>Qiymatni tasdiqlab elementni yakunlang. Sozlamaga qarab to‘g‘ridan-to‘g‘ri raqam kiritish yoqilgan bo‘lishi kerak.</li>
<li>Arrow bilan yaratilgan devorni tanlang. Bog‘langan o‘lcham yoki o‘lchash vositasi bilan 4000 mm ni tekshiring.</li>
<li>3D va kesimda balandlik, qalinlik va qavatga tegishliligini ko‘ring. Plan uzunligi to‘g‘ri, balandlik noto‘g‘ri bo‘lsa Wall Settingsdagi vertikal sozlamani tuzating.</li></ol>
<p><b>Tracker yo‘q bo‘lsa:</b> Options→Work Environment→Tracker and Coordinate Input sozlamasini tekshiring.
Distance/Angle va X/Y koordinatalarini aralashtirmang: birinchisi masofa va yo‘nalish, ikkinchisi koordinata qiymatlari.</p>
<p><b>Qayta sinash:</b> 5000 mm ikkinchi devor yarating. Qalinlik va balandlik o‘zgarmasin.
Ikki devor 4000/5000 mm bilan farqlanadi; bir parametrni o‘zgartirish boshqasini avtomatik o‘zgartirmaydi.</p>
<p>Archicad interfeysi til/versiyaga qarab farq qiladi.
<a href="https://help.graphisoft.com/AC/28/INT/_AC28_Help/030_Interaction/030_Interaction-40.htm">Tracker rasmiy qo‘llanmasi</a>
va <a href="https://help.graphisoft.com/AC/28/INT/_AC28_Help/040_ElementsVB/040_ElementsVB-7.htm">Wall Reference Line</a> bilan tekshiring.</p>
''',
'L07_M05_002': '''
<h3>Mezon va ustunni amalda ajratish</h3>
<p>Modelda D01=900 mm, D02=800 mm eshik va W01 deraza bor.
Scheme Settingsni oching. Criteria qismida element turini Door qilib belgilang.
Fields qismida ID va Widthni tanlang. Qo‘llangan scheme jadvalini oching.</p>
<table border="1" cellspacing="0" cellpadding="6"><tr><th>ID</th><th>Eni</th></tr><tr><td>D01</td><td>900 mm</td></tr><tr><td>D02</td><td>800 mm</td></tr></table>
<p><b>Sabab:</b> Door mezoni W01ni chiqarib tashlaydi. ID va Width esa tanlangan eshiklar haqida qaysi qiymat ko‘rsatilishini belgilaydi.</p>
<p><b>W01 ham ko‘rinsa:</b> Criteria element turini cheklamayotgan yoki boshqa mezon mantiqi aralashgan.
<b>En bo‘sh bo‘lsa:</b> Width field manbasi va element parametrini tekshiring.
<b>Ikkita eshik bitta satr bo‘lsa:</b> grouping va birlashtirish sozlamasini tekshiring; elementni o‘chirmang.</p>
<p><b>Mashq yechimi:</b> D03=1000 mm eshik qo‘shing. Door mezonida uch eshik chiqadi, W01 chiqmaydi.
Width ustuni kerak bo‘lmasa fielddan olib tashlang: eshiklar soni uchligicha qoladi.
Bu mezon va ustun boshqa vazifa bajarishini isbotlaydi.</p>
''',
'L12_M07_002': '''
<h3>Ikki varaqni boshqariladigan PDF paketga chiqarish</h3>
<p>Layout Bookda A-01 plan va A-02 kesim tayyor bo‘lsin. Publisherda Client_PDF to‘plamini yarating.
Kerakli ikki layoutni tartib bilan to‘plamga kiriting. Publishing Propertiesda Save usulini va destinationni belgilang,
PDF output sozlamasini tekshiring. Kerak bo‘lsa birlashtirilgan fayl chiqarish variantini tanlang.</p>
<p>Fayl nomi HOUSE_R02.pdf bo‘lsin. Publishdan keyin faylni alohida oching.
A-01 va A-02 mavjudmi, tartib to‘g‘rimi, chizma va shtamp o‘qiladimi, revision mosmi — tekshiring.</p>
<p><b>Yechim:</b> ikki layout qo‘shilgan bo‘lsa kutilgan paket ikki varaqni qamraydi.
Bir varaq yetishmasa Publisher Set tarkibi va chiqarish qamrovini tekshiring.
Fayl topilmasa destinationni tekshiring; modelni qayta chizish kerak emas.</p>
<p><b>Mustaqil variant:</b> A-03 fasadni qo‘shing, tartibni plan→fasad→kesim qiling.
Yangi paket uch varaq bo‘lishi va belgilangan tartibni saqlashi kerak.</p>
'''
}
