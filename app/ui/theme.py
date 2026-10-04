from PySide6.QtCore import (
    Qt,
)

from PySide6.QtWidgets import (
    QApplication,
    QAbstractScrollArea,
    QFrame,
    QScrollArea,
    QWidget,
)
from PySide6.QtGui import QColor, QPalette


CREAM = "#F5F1E7"
PAPER = "#FFFDF7"
INK = "#203B36"
TEAL = "#0E5558"
COPPER = "#A65D35"


def install_application_theme(app):
    """Keep native dialogs, menus and input controls in the same paper palette."""
    palette = QPalette()
    roles = {
        QPalette.ColorRole.Window: CREAM,
        QPalette.ColorRole.WindowText: INK,
        QPalette.ColorRole.Base: PAPER,
        QPalette.ColorRole.AlternateBase: CREAM,
        QPalette.ColorRole.Text: INK,
        QPalette.ColorRole.Button: PAPER,
        QPalette.ColorRole.ButtonText: INK,
        QPalette.ColorRole.Highlight: TEAL,
        QPalette.ColorRole.HighlightedText: PAPER,
        QPalette.ColorRole.ToolTipBase: PAPER,
        QPalette.ColorRole.ToolTipText: INK,
        QPalette.ColorRole.Link: TEAL,
    }
    for role, color in roles.items():
        palette.setColor(role, QColor(color))
    for role in (QPalette.ColorRole.Text, QPalette.ColorRole.WindowText,
                 QPalette.ColorRole.ButtonText):
        palette.setColor(QPalette.ColorGroup.Disabled, role, QColor("#737C72"))
    app.setPalette(palette)
    app.setStyleSheet("""
        QToolTip { background-color: #FFFDF7; color: #203B36;
                   border: 1px solid #D5CBBB; padding: 6px; }
        QMenu { background-color: #FFFDF7; color: #203B36;
                border: 1px solid #D5CBBB; }
        QMenu::item:selected { background-color: #0E5558; color: #FFFDF7; }
        QMessageBox, QFileDialog, QInputDialog { background-color: #F5F1E7; }
    """)


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
    background-color: #F5F1E7;
}

QWidget {
    font-family: "Segoe UI";
    color: #0E5558;
}


/* ==========================================================
   SIDEBAR
   ========================================================== */

QFrame#sidebar {
    background-color: #F5F1E7;
    border-right: 1px solid #D5CBBB;
}

QLabel#logo {
    color: #0E5558;
    font-size: 25px;
    font-weight: 800;

                font-family: "Georgia";
}

QLabel#logoSub {
    color: #586B64;
    font-size: 13px;
}

QListWidget {
    background-color: transparent;
    border: none;
    outline: none;

    color: #203B36;

    font-size: 15px;
    font-weight: 500;
}

QListWidget::item {
    padding: 12px 14px;
    margin: 2px 0px;

    border-radius: 9px;
}

QListWidget::item:hover {
    background-color: #FFFDF7;
    color: #203B36;
}

QListWidget::item:selected {
    background-color: #0E5558;
    color: #FFFDF7;
}


/* ==========================================================
   OVERVIEW HEADER
   ========================================================== */

QFrame#overviewHeader {
    background-color: #FFFDF7;
    border: 1px solid #D5CBBB;
    border-bottom: 3px solid #A65D35;
    border-radius: 16px;
}

QLabel#overviewTitle {
    color: #0E5558;

    font-size: 30px;
    font-weight: 800;

                font-family: "Georgia";
}

QLabel#overviewSubtitle {
    color: #586B64;

    font-size: 15px;
}


/* ==========================================================
   LEVEL OVERVIEW CARDS
   ========================================================== */

QFrame#levelOverviewCard {
    background-color: #FFFDF7;

    border: 1px solid #D5CBBB;
    border-radius: 15px;
}

QFrame#levelOverviewCard:hover {
    background-color: #FFFDF7;

    border: 1px solid #4B7B78;
}

QLabel#levelCode {
    color: #0E5558;

    font-size: 13px;
    font-weight: 800;
}

QLabel#levelName {
    color: #0E5558;

    font-size: 20px;
    font-weight: 750;

                font-family: "Georgia";
}

QLabel#levelDesc {
    color: #586B64;

    font-size: 14px;
}

QLabel#progressText {
    color: #203B36;

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
    background-color: #FFFDF7;

    border: 1px solid #D5CBBB;

    color: #586B64;
}

QLabel#statusBadgeAvailable {
    background-color: #FFFDF7;

    border: 1px solid #4B7B78;

    color: #0E5558;
}

QLabel#statusBadgeCompleted {
    background-color: #E7F0E8;

    border: 1px solid #D5CBBB;

    color: #27624A;
}

QLabel#statusBadgeMaster {
    background-color: #F4E9D7;

    border: 1px solid #A65D35;

    color: #A65D35;
}


/* ==========================================================
   LEVEL BUTTON
   ========================================================== */

QPushButton#openLevelButton {
    background-color: #FFFDF7;

    border: 1px solid #D5CBBB;
    border-radius: 9px;

    color: #0E5558;

    min-height: 36px;

    padding-left: 15px;
    padding-right: 15px;

    font-size: 13px;
    font-weight: 700;
}

QPushButton#openLevelButton:hover {
    background-color: #FFFDF7;

    border: 1px solid #4B7B78;

    color: #203B36;
}


/* ==========================================================
   LEARNING PAGE
   ========================================================== */

QLabel#pageTitle {
    color: #0E5558;

    font-size: 31px;
    font-weight: 800;

                font-family: "Georgia";
}

QLabel#pageSubtitle {
    color: #586B64;

    font-size: 15px;
}

QFrame#levelCard,
QFrame#levelLocked,
QFrame#levelCompleted,
QFrame#levelMaster {
    background-color: #FFFDF7;

    border: 1px solid #D5CBBB;

    border-radius: 15px;
}

QFrame#levelCompleted {
    border-color: #D5CBBB;
}

QFrame#levelMaster {
    border-color: #A65D35;
}

QLabel#levelTitle {
    color: #0E5558;

    font-size: 22px;
    font-weight: 800;

                font-family: "Georgia";
}

QLabel#levelSubtitle {
    color: #586B64;

    font-size: 14px;
}


/* ==========================================================
   MODULE CARDS
   ========================================================== */

QFrame#moduleCard {
    background-color: #FFFDF7;

    border: 1px solid #D5CBBB;

    border-radius: 13px;
}

QLabel#moduleTitle {
    color: #0E5558;

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
    background-color: #FFFDF7;

    border: 1px solid #D5CBBB;

    border-radius: 10px;
}

QFrame#lessonLocked {
    background-color: #FFFDF7;

    border-color: #D5CBBB;
}

QFrame#lessonAvailable {
    background-color: #FFFDF7;

    border-color: #4B7B78;
}

QFrame#lessonCompleted {
    background-color: #E7F0E8;

    border-color: #D5CBBB;
}

QFrame#lessonMaster {
    background-color: #F5F1E7;

    border-color: #D5CBBB;
}

QLabel#lessonTitle {
    color: #0E5558;

    font-size: 15px;
    font-weight: 650;
}

QLabel#meta {
    color: #586B64;

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
    background-color: #0E5558;

    border: 1px solid #4B7B78;
    border-radius: 9px;

    color: #FFFDF7;

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
    background-color: #0E5558;
}


/* ==========================================================
   SECONDARY BUTTON
   ========================================================== */

QPushButton#backButton,
QPushButton#embeddedBackButton {
    background-color: #FFFDF7;

    border: 1px solid #D5CBBB;
    border-radius: 9px;

    color: #203B36;

    min-height: 34px;

    padding-left: 15px;
    padding-right: 15px;

    font-size: 13px;
    font-weight: 650;
}

QPushButton#backButton:hover,
QPushButton#embeddedBackButton:hover {
    background-color: #FFFDF7;

    border-color: #D5CBBB;
}


/* ==========================================================
   PROGRESS
   ========================================================== */

QProgressBar {
    background-color: #FFFDF7;

    border: none;
    border-radius: 5px;

    min-height: 9px;
    max-height: 9px;

    color: transparent;
}

QProgressBar::chunk {
    background-color: #0E5558;

    border-radius: 5px;
}


/* ==========================================================
   SCROLL AREAS
   ========================================================== */

QScrollArea,
QAbstractScrollArea {
    background-color: #F5F1E7;

    border: none;
}

QAbstractScrollArea::viewport {
    background-color: #F5F1E7;
}

QWidget#overviewContent {
    background-color: #F5F1E7;
}


/* ==========================================================
   SCROLL BAR
   ========================================================== */

QScrollBar:vertical {
    background-color: #F5F1E7;

    width: 11px;

    margin: 3px;

    border: none;
}

QScrollBar::handle:vertical {
    background-color: #BDB29E;

    min-height: 45px;

    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background-color: #A65D35;
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
    background-color: #FFFDF7;

    border: 1px solid #D5CBBB;
    border-radius: 10px;

    padding: 10px;

    color: #203B36;

    font-size: 12px;
}
"""


def fix_scroll_surfaces(
    root: QWidget,
):
    """
    Scroll area'larni performance-safe sozlaydi.

    MUHIM:
    viewport yoki content widget'ga inline stylesheet
    qo'llanmaydi. Aks holda Qt stylesheet inheritance
    sabab module/lesson kartalarining border/background
    dizayni yo'qolishi mumkin.
    """

    if root is None:
        return

    for scroll in root.findChildren(
        QScrollArea
    ):
        scroll.setFrameShape(
            QFrame.Shape.NoFrame
        )

        scroll.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )

        scroll.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )


def install_premium_theme(
    root: QWidget,
):
    """
    Theme faqat BIR MARTA shell'ga qo'llanadi.
    """

    if root is None:
        return

    app = QApplication.instance()
    if app is not None and not app.property("archiproPaperTheme"):
        install_application_theme(app)
        app.setProperty("archiproPaperTheme", True)

    root.setStyleSheet(
        APP_QSS
    )

    fix_scroll_surfaces(
        root
    )
