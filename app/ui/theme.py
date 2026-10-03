from PySide6.QtWidgets import (
    QAbstractScrollArea,
    QScrollArea,
    QWidget,
)


# ============================================================
# ARCHIPRO UZ — UI V3
# PERFORMANCE-SAFE THEME
# ============================================================

APP_QSS = """
/* ==========================================================
   ROOT
   ========================================================== */

QMainWindow,
QWidget#appRoot,
QStackedWidget {
    background-color: #08111F;
}

QWidget {
    font-family: "Segoe UI";
    color: #E5EDF7;
}


/* ==========================================================
   SIDEBAR
   ========================================================== */

QFrame#sidebar {
    background-color: #0A1424;
    border-right: 1px solid #25364E;
}

QLabel#logo {
    color: #F4F8FC;
    font-size: 25px;
    font-weight: 800;
}

QLabel#logoSub {
    color: #7E90A8;
    font-size: 13px;
}

QListWidget {
    background-color: transparent;
    border: none;
    outline: none;

    color: #C7D2E0;

    font-size: 15px;
    font-weight: 500;
}

QListWidget::item {
    padding: 12px 14px;
    margin: 2px 0px;

    border-radius: 9px;
}

QListWidget::item:hover {
    background-color: #14233A;
    color: #FFFFFF;
}

QListWidget::item:selected {
    background-color: #2F68D8;
    color: #FFFFFF;
}


/* ==========================================================
   OVERVIEW HEADER
   ========================================================== */

QFrame#overviewHeader {
    background-color: #0E1B2E;

    border: 1px solid #29415F;
    border-radius: 16px;
}

QLabel#overviewTitle {
    color: #F5F8FC;

    font-size: 30px;
    font-weight: 800;
}

QLabel#overviewSubtitle {
    color: #9DACBF;

    font-size: 15px;
}


/* ==========================================================
   LEVEL OVERVIEW CARDS
   ========================================================== */

QFrame#levelOverviewCard {
    background-color: #0E1A2C;

    border: 1px solid #263C58;
    border-radius: 15px;
}

QFrame#levelOverviewCard:hover {
    background-color: #112039;

    border: 1px solid #395C89;
}

QLabel#levelCode {
    color: #6598FF;

    font-size: 13px;
    font-weight: 800;
}

QLabel#levelName {
    color: #F1F5FA;

    font-size: 20px;
    font-weight: 750;
}

QLabel#levelDesc {
    color: #95A6BC;

    font-size: 14px;
}

QLabel#progressText {
    color: #AAB8C9;

    font-size: 13px;
    font-weight: 600;
}


/* ==========================================================
   STATUS PILLS
   ========================================================== */

QLabel#statusBadgeLocked,
QLabel#statusBadgeAvailable,
QLabel#statusBadgeCompleted,
QLabel#statusBadgeMaster {
    border-radius: 8px;

    padding: 6px 10px;

    font-size: 12px;
    font-weight: 800;
}

QLabel#statusBadgeLocked {
    background-color: #151D2A;

    border: 1px solid #37465B;

    color: #9AA8BA;
}

QLabel#statusBadgeAvailable {
    background-color: #102443;

    border: 1px solid #356FD8;

    color: #8AB4FF;
}

QLabel#statusBadgeCompleted {
    background-color: #10271F;

    border: 1px solid #2E7257;

    color: #7BDAAD;
}

QLabel#statusBadgeMaster {
    background-color: #2B230D;

    border: 1px solid #947428;

    color: #F1CA64;
}


/* ==========================================================
   LEVEL BUTTON
   ========================================================== */

QPushButton#openLevelButton {
    background-color: #182942;

    border: 1px solid #385679;
    border-radius: 9px;

    color: #DCE7F5;

    min-height: 36px;

    padding-left: 15px;
    padding-right: 15px;

    font-size: 13px;
    font-weight: 700;
}

QPushButton#openLevelButton:hover {
    background-color: #22416C;

    border: 1px solid #4F84CF;

    color: #FFFFFF;
}


/* ==========================================================
   LEARNING PAGE
   ========================================================== */

QLabel#pageTitle {
    color: #F5F8FC;

    font-size: 31px;
    font-weight: 800;
}

QLabel#pageSubtitle {
    color: #9DACBF;

    font-size: 15px;
}

QFrame#levelCard,
QFrame#levelLocked,
QFrame#levelCompleted,
QFrame#levelMaster {
    background-color: #0D192A;

    border: 1px solid #29405D;

    border-radius: 15px;
}

QFrame#levelCompleted {
    border-color: #2C6D54;
}

QFrame#levelMaster {
    border-color: #886D2C;
}

QLabel#levelTitle {
    color: #F3F7FB;

    font-size: 22px;
    font-weight: 800;
}

QLabel#levelSubtitle {
    color: #98A8BC;

    font-size: 14px;
}


/* ==========================================================
   MODULE CARDS
   ========================================================== */

QFrame#moduleCard {
    background-color: #101D30;

    border: 1px solid #253A56;

    border-radius: 13px;
}

QLabel#moduleTitle {
    color: #EDF3F9;

    font-size: 18px;
    font-weight: 700;
}


/* ==========================================================
   LESSON ROWS
   ========================================================== */

QFrame#lessonLocked,
QFrame#lessonAvailable,
QFrame#lessonCompleted,
QFrame#lessonMaster {
    background-color: #0D192A;

    border: 1px solid #23364F;

    border-radius: 10px;
}

QFrame#lessonLocked {
    background-color: #0C1727;

    border-color: #1F3046;
}

QFrame#lessonAvailable {
    background-color: #102441;

    border-color: #3974D9;
}

QFrame#lessonCompleted {
    background-color: #10251F;

    border-color: #2E7056;
}

QFrame#lessonMaster {
    background-color: #211D11;

    border-color: #7D662E;
}

QLabel#lessonTitle {
    color: #E4EBF4;

    font-size: 15px;
    font-weight: 650;
}

QLabel#meta {
    color: #8193AA;

    font-size: 12px;
}


/* ==========================================================
   ACTION BUTTONS
   ========================================================== */

QPushButton#openLesson,
QPushButton#reviewLesson,
QPushButton#examButton,
QPushButton#primaryButton,
QPushButton#quizButton,
QPushButton#submitButton {
    background-color: #356FE0;

    border: 1px solid #528DFA;
    border-radius: 9px;

    color: #FFFFFF;

    min-height: 36px;

    padding-left: 17px;
    padding-right: 17px;

    font-size: 13px;
    font-weight: 750;
}

QPushButton#openLesson:hover,
QPushButton#reviewLesson:hover,
QPushButton#examButton:hover,
QPushButton#primaryButton:hover,
QPushButton#quizButton:hover,
QPushButton#submitButton:hover {
    background-color: #477FE5;
}


/* ==========================================================
   SECONDARY BUTTON
   ========================================================== */

QPushButton#backButton,
QPushButton#embeddedBackButton {
    background-color: #15243A;

    border: 1px solid #2C405D;
    border-radius: 9px;

    color: #D8E1EC;

    min-height: 34px;

    padding-left: 15px;
    padding-right: 15px;

    font-size: 13px;
    font-weight: 650;
}

QPushButton#backButton:hover,
QPushButton#embeddedBackButton:hover {
    background-color: #1C304C;

    border-color: #496786;
}


/* ==========================================================
   PROGRESS
   ========================================================== */

QProgressBar {
    background-color: #17263A;

    border: none;
    border-radius: 5px;

    min-height: 9px;
    max-height: 9px;

    color: transparent;
}

QProgressBar::chunk {
    background-color: #4F86EB;

    border-radius: 5px;
}


/* ==========================================================
   SCROLL AREAS
   ========================================================== */

QScrollArea,
QAbstractScrollArea {
    background-color: #08111F;

    border: none;
}

QAbstractScrollArea::viewport {
    background-color: #08111F;
}

QWidget#overviewContent {
    background-color: #08111F;
}


/* ==========================================================
   SCROLL BAR
   ========================================================== */

QScrollBar:vertical {
    background-color: #0B1627;

    width: 11px;

    margin: 3px;

    border: none;
}

QScrollBar::handle:vertical {
    background-color: #344B68;

    min-height: 45px;

    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background-color: #486584;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {
    height: 0px;
}

QScrollBar::add-page:vertical,
QScrollBar::sub-page:vertical {
    background: none;
}


/* ==========================================================
   USER / DEVELOPER
   ========================================================== */

QLabel#userInfo {
    background-color: #101C2E;

    border: 1px solid #263A54;
    border-radius: 10px;

    padding: 10px;

    color: #C8D4E3;

    font-size: 12px;
}
"""


def fix_scroll_surfaces(
    root: QWidget,
):
    """
    Faqat sahifa yaratilganda chaqiriladi.
    EventFilter yo'q.
    """

    if root is None:
        return

    for scroll in root.findChildren(
        QScrollArea
    ):
        scroll.setStyleSheet(
            scroll.styleSheet()
            + """
            QScrollArea {
                background-color: #08111F;
                border: none;
            }

            QAbstractScrollArea::viewport {
                background-color: #08111F;
            }
            """
        )

        viewport = scroll.viewport()

        if viewport is not None:
            viewport.setStyleSheet(
                "background-color: #08111F;"
            )

        content = scroll.widget()

        if content is not None:
            content.setStyleSheet(
                content.styleSheet()
                + """
                background-color: #08111F;
                """
            )


def install_premium_theme(
    root: QWidget,
):
    """
    Theme faqat BIR MARTA shell'ga qo'llanadi.
    """

    if root is None:
        return

    root.setStyleSheet(
        APP_QSS
    )

    fix_scroll_surfaces(
        root
    )
