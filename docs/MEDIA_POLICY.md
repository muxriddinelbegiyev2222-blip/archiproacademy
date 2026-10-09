# Dars tasvirlari hajmi va sifat talabi

- Har bir yangi yoki qayta siqilgan dars tasviri **400 000 baytdan oshmasin**.
- Tasvir o‘lchami imkon qadar asl piksel o‘lchamida saqlanadi. Hozirgi siqish bosqichi piksel o‘lchamini o‘zgartirmaydi.
- Arxitektura eskizlari uchun shu chegara ichidagi eng yuqori JPEG sifati, 4:4:4 rang va optimallashtirilgan kodlash ishlatiladi.
- Haqiqiy dastur skrinshotlari o‘qiladigan matn va interfeys chegaralari saqlangan PNG ko‘rinishida qoladi.
- Katta PNG/JPEG tasvirni SVG ichiga base64 shaklida joylash yangi eskizlar uchun ishlatilmaydi.
- Asl katta generatsiya nusxalari, vaqtinchalik taqqoslash fayllari va build arxivlari Git manba reyestriga qo‘shilmaydi.
- Har bir partiya: mavzu mosligi, o‘zbekcha izoh, mayda chiziq va yozuvlar, Qt orqali ochilish, dars bog‘lanishi va fayl hajmi bilan tekshiriladi.
- JPEG siqish matematik jihatdan yo‘qotishli. Tiniqlikni tekshirmasdan “sifat mutlaqo yo‘qolmagan” deb hisoblanmaydi.
- Oddiy commitlar Windows paketini qurib tekshiradi; yuklab olinadigan build arxivi faqat qo‘lda ishga tushirilgan reliz tekshiruvida 3 kun saqlanadi.
- Joriy faylni kichraytirish tarixdagi katta nusxani o‘chirmaydi. Tarixni qayta yozishdan oldin barcha branch uchlari va joriy daraxt qayd etiladi; kod mazmuni hamda joriy ixcham tasvirlar o‘zgarmagani tekshiriladi.
