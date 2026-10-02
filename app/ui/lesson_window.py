from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)


class LessonWindow(QMainWindow):
    def __init__(self, lesson: dict):
        super().__init__()

        self.lesson = lesson

        self.setWindowTitle(
            f"ARCHIPRO UZ - {lesson.get('title', 'Dars')}"
        )
        self.resize(1200, 800)

        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #0B1220;
            }

            QWidget {
                font-family: Segoe UI;
                color: #F8FAFC;
            }

            QLabel#lessonLevel {
                color: #60A5FA;
                font-size: 13px;
                font-weight: 600;
            }

            QLabel#lessonTitle {
                color: #FFFFFF;
                font-size: 32px;
                font-weight: 700;
            }

            QLabel#lessonMeta {
                color: #94A3B8;
                font-size: 13px;
            }

            QFrame#contentCard {
                background-color: #111827;
                border: 1px solid #1E293B;
                border-radius: 16px;
            }

            QLabel#sectionTitle {
                color: #FFFFFF;
                font-size: 20px;
                font-weight: 700;
            }

            QLabel#bodyText {
                color: #CBD5E1;
                font-size: 15px;
            }

            QFrame#highlightCard {
                background-color: #13213A;
                border: 1px solid #1D4ED8;
                border-radius: 12px;
            }

            QFrame#exampleCard {
                background-color: #12221B;
                border: 1px solid #166534;
                border-radius: 12px;
            }

            QFrame#warningCard {
                background-color: #281B16;
                border: 1px solid #9A3412;
                border-radius: 12px;
            }

            QPushButton#backButton {
                background-color: #1E293B;
                color: #E2E8F0;
                border: none;
                border-radius: 9px;
                padding: 10px 18px;
                font-size: 14px;
            }

            QPushButton#backButton:hover {
                background-color: #334155;
            }

            QPushButton#completeButton {
                background-color: #2563EB;
                color: white;
                border: none;
                border-radius: 9px;
                padding: 12px 20px;
                font-size: 14px;
                font-weight: 600;
            }

            QPushButton#completeButton:hover {
                background-color: #3B82F6;
            }
            """
        )

        central = QWidget()
        self.setCentralWidget(central)

        root_layout = QVBoxLayout(central)
        root_layout.setContentsMargins(35, 25, 35, 25)
        root_layout.setSpacing(18)

        # HEADER
        top_bar = QHBoxLayout()

        back_button = QPushButton("← ORQAGA")
        back_button.setObjectName("backButton")
        back_button.clicked.connect(self.close)

        top_bar.addWidget(back_button)
        top_bar.addStretch()

        root_layout.addLayout(top_bar)

        level_label = QLabel(
            lesson.get(
                "level_title",
                "ARCHIPRO UZ"
            )
        )
        level_label.setObjectName("lessonLevel")

        title_label = QLabel(
            lesson.get(
                "title",
                "Dars"
            )
        )
        title_label.setObjectName("lessonTitle")
        title_label.setWordWrap(True)

        module_title = lesson.get(
            "module_title",
            ""
        )

        lesson_type = lesson.get(
            "lesson_type",
            "theory"
        )

        minutes = lesson.get(
            "estimated_minutes",
            10
        )

        meta_label = QLabel(
            f"{module_title}   •   "
            f"{lesson_type.upper()}   •   "
            f"{minutes} daqiqa"
        )
        meta_label.setObjectName("lessonMeta")

        root_layout.addWidget(level_label)
        root_layout.addWidget(title_label)
        root_layout.addWidget(meta_label)

        # SCROLL CONTENT
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QScrollArea.Shape.NoFrame)

        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(0, 10, 15, 25)
        scroll_layout.setSpacing(18)

        # ASOSIY KONTENT
        if lesson.get("code") == "L00_M01_001":
            self.build_first_lesson(
                scroll_layout
            )
        else:
            self.build_default_lesson(
                scroll_layout
            )

        scroll_layout.addStretch()

        scroll.setWidget(scroll_content)

        root_layout.addWidget(scroll, 1)

        complete_button = QPushButton(
            "DARSNI TUGATISH"
        )
        complete_button.setObjectName(
            "completeButton"
        )
        complete_button.setFixedWidth(190)

        root_layout.addWidget(
            complete_button,
            alignment=Qt.AlignmentFlag.AlignRight,
        )

    def create_card(
        self,
        title: str,
        text: str,
        object_name: str = "contentCard",
    ) -> QFrame:

        card = QFrame()
        card.setObjectName(object_name)

        layout = QVBoxLayout(card)
        layout.setContentsMargins(
            24,
            22,
            24,
            22,
        )
        layout.setSpacing(10)

        title_label = QLabel(title)
        title_label.setObjectName(
            "sectionTitle"
        )

        body_label = QLabel(text)
        body_label.setObjectName(
            "bodyText"
        )
        body_label.setWordWrap(True)
        body_label.setTextFormat(
            Qt.TextFormat.RichText
        )

        layout.addWidget(title_label)
        layout.addWidget(body_label)

        return card

    def build_first_lesson(
        self,
        layout: QVBoxLayout,
    ):
        layout.addWidget(
            self.create_card(
                "Bugun nimani o'rganamiz?",
                """
                Bu darsdan keyin siz <b>arxitektura nima</b>,
                arxitektor faqat chiroyli uy chizadigan odam
                emasligini va yaxshi uy loyihasi nimadan
                boshlanishini tushunasiz.
                """,
                "highlightCard",
            )
        )

        layout.addWidget(
            self.create_card(
                "Arxitektura nima?",
                """
                Juda sodda qilib aytganda, arxitektura —
                <b>odam yashashi, ishlashi yoki dam olishi uchun
                qulay, xavfsiz va chiroyli makon yaratish</b>.

                <br><br>

                Masalan, siz 200 m² uy qurdingiz.
                Uy tashqaridan juda chiroyli bo'lishi mumkin.
                Lekin oshxonadan ovqatni mehmonxonaga olib
                borish uchun uzun koridordan o'tish kerak bo'lsa,
                yotoqxona eshigi to'g'ridan-to'g'ri mehmonxonaga
                ochilsa yoki sanuzel juda noqulay joylashsa —
                bu yaxshi arxitektura emas.

                <br><br>

                Demak, arxitekturada faqat
                <b>“qanday ko'rinadi?”</b> degan savol emas,
                <b>“undan foydalanish qanchalik qulay?”</b>
                degan savol ham juda muhim.
                """,
            )
        )

        layout.addWidget(
            self.create_card(
                "Tasavvur qiling",
                """
                Sizga mijoz keldi va dedi:

                <br><br>

                <b>
                “Menda 20 × 30 metr yer bor.
                Oilamiz 4 kishi.
                3 ta yotoqxona, katta mehmonxona,
                oshxona va 2 ta sanuzel kerak.”
                </b>

                <br><br>

                Boshlovchi odam darhol devor chizishni boshlashi
                mumkin.

                <br><br>

                Arxitektor esa avval savol beradi:

                <br>
                • Ko'cha qaysi tomonda?<br>
                • Quyosh qayerdan tushadi?<br>
                • Mashina qayerdan kiradi?<br>
                • Mehmonlar qaysi zonaga kiradi?<br>
                • Oila a'zolarining private zonasi qayerda bo'ladi?<br>
                • Hovlining qaysi qismi ko'proq ishlatiladi?

                <br><br>

                Mana shu — <b>arxitektor kabi fikrlashning
                boshlanishi</b>.
                """,
                "exampleCard",
            )
        )

        layout.addWidget(
            self.create_card(
                "Muhim qoida",
                """
                <b>
                Yaxshi loyiha chizishdan oldin
                yaxshi savollar berish kerak.
                </b>

                <br><br>

                Archicad sizga devor chizib beradi.
                Lekin devorni <b>qayerga va nima uchun</b>
                qo'yishni arxitektor hal qiladi.
                """,
                "highlightCard",
            )
        )

        layout.addWidget(
            self.create_card(
                "Boshlovchilar qiladigan xato",
                """
                Eng ko'p uchraydigan xato —
                <b>fasadni o'ylab, planni unutish</b>.

                <br><br>

                Uy tashqaridan juda chiroyli ko'rinishi mumkin,
                lekin ichida yashash noqulay bo'lsa,
                loyiha muvaffaqiyatli hisoblanmaydi.

                <br><br>

                Biz kurs davomida avval
                <b>to'g'ri fikrlashni</b>,
                keyin esa uni Archicad orqali
                professional chizmaga aylantirishni o'rganamiz.
                """,
                "warningCard",
            )
        )

        layout.addWidget(
            self.create_card(
                "2 daqiqalik mini-amaliyot",
                """
                O'zingiz yashayotgan uyni eslang.

                <br><br>

                Quyidagi savollarga fikran javob bering:

                <br><br>

                1. Uyga kirganda birinchi qaysi xona ko'rinadi?<br>
                2. Oshxonadan mehmonxonaga yurish qulaymi?<br>
                3. Yotoqxona private joydami?<br>
                4. Uyda keraksiz uzun koridor bormi?<br>
                5. Siz o'zgartirmoqchi bo'lgan bitta joy qaysi?

                <br><br>

                Siz hozirning o'zida uyga oddiy foydalanuvchi
                sifatida emas, <b>arxitektor ko'zi bilan</b>
                qarashni boshladingiz.
                """,
                "exampleCard",
            )
        )

        layout.addWidget(
            self.create_card(
                "Dars xulosasi",
                """
                Bugun 3 ta asosiy fikrni eslab qoling:

                <br><br>

                <b>1.</b> Arxitektura faqat chiroyli bino emas.<br>
                <b>2.</b> Qulaylik va funksiya juda muhim.<br>
                <b>3.</b> Professional loyiha savol va
                tahlildan boshlanadi.

                <br><br>

                Keyingi darsda:
                <b>“Arxitektor kim va uning vazifasi nima?”</b>
                mavzusini o'rganamiz.
                """,
                "highlightCard",
            )
        )

    def build_default_lesson(
        self,
        layout: QVBoxLayout,
    ):
        summary = self.lesson.get(
            "summary",
            "Ushbu dars kontenti tayyorlanmoqda."
        )

        layout.addWidget(
            self.create_card(
                "Dars haqida",
                summary,
            )
        )
