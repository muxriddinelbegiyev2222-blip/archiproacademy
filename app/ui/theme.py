from PySide6.QtCore import (
    QEvent,
    QObject,
    QTimer,
)

from PySide6.QtWidgets import (
    QAbstractScrollArea,
    QApplication,
    QScrollArea,
    QWidget,
)


# ============================================================
# ARCHIPRO UZ — PREMIUM DARK UI
# ============================================================

BACKGROUND = "#08111F"
SURFACE = "#0C1728"
SURFACE_2 = "#111E31"
SURFACE_3 = "#15243A"

BORDER = "#22324A"
BORDER_ACTIVE = "#386FD8"

TEXT = "#EAF1FA"
TEXT_SOFT = "#C8D3E1"
MUTED = "#91A2BA"

ACCENT = "#4F8CFF"
ACCENT_HOVER = "#6BA0FF"

SUCCESS = "#42C98B"
WARNING = "#E8B84D"
DANGER = "#E47070"


PREMIUM_QSS = """
/* ==========================================================
   BASE
   ========================================================== */

QMainWindow {
    background-color: #08111F;
}

QWidget {
    font-family: "Segoe UI";
    color: #EAF1FA;
}

QWidget#appRoot {
    background-color: #08111F;
}

QStackedWidget {
    background-color: #08111F;
    border: none;
}


/* ==========================================================
   SIDEBAR
   ========================================================== */

QFrame#sidebar {
    background-color: #0A1424;
    border-right: 1px solid #22324A;
}

QLabel#logo {
    color: #F4F7FB;
    font-size: 25px;
    font-weight: 800;
}

QLabel#logoSub {
    color: #788BA6;
    font-size: 13px;
}

QListWidget {
    background: transparent;
    border: none;
    outline: none;
    color: #C8D3E1;
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
    background-color: #295FC8;
    color: #FFFFFF;
}


/* ==========================================================
   COMMON TITLES
   ========================================================== */

QLabel#pageTitle {
    color: #F4F7FB;
    font-size: 34px;
    font-weight: 800;
}

QLabel#pageSubtitle {
    color: #9BAAC0;
    font-size: 16px;
}

QLabel#levelTitle {
    color: #F4F7FB;
    font-size: 23px;
    font-weight: 800;
}

QLabel#levelSubtitle {
    color: #9BAAC0;
    font-size: 15px;
}

QLabel#moduleTitle {
    color: #EDF3FA;
    font-size: 19px;
    font-weight: 700;
}

QLabel#lessonTitle {
    color: #E7EEF8;
    font-size: 16px;
    font-weight: 600;
}

QLabel#meta {
    color: #8396AF;
    font-size: 13px;
}


/* ==========================================================
   LEARNING CARDS
   ========================================================== */

QFrame#levelCard,
QFrame#levelLocked,
QFrame#levelCompleted,
QFrame#levelMaster {
    background-color: #0C1728;
    border: 1px solid #263852;
    border-radius: 16px;
}

QFrame#levelCompleted {
    border: 1px solid #27624D;
}

QFrame#levelMaster {
    border: 1px solid #866927;
}

QFrame#moduleCard {
    background-color: #101C2F;
    border: 1px solid #223650;
    border-radius: 13px;
}

QFrame#lessonLocked,
QFrame#lessonAvailable,
QFrame#lessonCompleted,
QFrame#lessonMaster {
    background-color: #0E1A2C;
    border: 1px solid #20334D;
    border-radius: 10px;
}

QFrame#lessonAvailable {
    background-color: #102343;
    border: 1px solid #386FD8;
}

QFrame#lessonCompleted {
    background-color: #10251F;
    border: 1px solid #27624D;
}

QFrame#lessonMaster {
    border: 1px solid #806A2E;
}


/* ==========================================================
   EXAMS
   ========================================================== */

QFrame#examLocked,
QFrame#examAvailable,
QFrame#examCompleted,
QFrame#examMaster {
    background-color: #101C2F;
    border: 1px solid #253A56;
    border-radius: 13px;
}

QFrame#examAvailable {
    border: 1px solid #9B762B;
}

QFrame#examCompleted {
    border: 1px solid #27624D;
}


/* ==========================================================
   BUTTONS
   ========================================================== */

QPushButton {
    min-height: 36px;
    border-radius: 9px;
    font-size: 14px;
    font-weight: 650;
}

QPushButton#openLesson,
QPushButton#reviewLesson,
QPushButton#examButton,
QPushButton#primaryButton,
QPushButton#quizButton,
QPushButton#submitButton {
    background-color: #356FE0;
    border: 1px solid #4F8CFF;
    color: #FFFFFF;
    padding: 9px 18px;
}

QPushButton#openLesson:hover,
QPushButton#reviewLesson:hover,
QPushButton#examButton:hover,
QPushButton#primaryButton:hover,
QPushButton#quizButton:hover,
QPushButton#submitButton:hover {
    background-color: #467FE8;
}

QPushButton#backButton,
QPushButton#embeddedBackButton {
    background-color: #15243A;
    border: 1px solid #2A3D59;
    color: #DCE5F1;
    padding: 8px 16px;
}

QPushButton#backButton:hover,
QPushButton#embeddedBackButton:hover {
    background-color: #1B2E49;
    border-color: #3C5576;
}


/* ==========================================================
   SCROLL AREA — WHITE BACKGROUND FIX
   ========================================================== */

QScrollArea,
QAbstractScrollArea {
    background-color: #08111F;
    border: none;
}

QAbstractScrollArea::viewport {
    background-color: #08111F;
}

QScrollArea > QWidget {
    background-color: #08111F;
}

QScrollArea > QWidget > QWidget {
    background-color: #08111F;
}


/* ==========================================================
   SCROLLBAR
   ========================================================== */

QScrollBar:vertical {
    background-color: #0B1627;
    width: 12px;
    margin: 3px;
    border: none;
}

QScrollBar::handle:vertical {
    background-color: #314561;
    min-height: 45px;
    border-radius: 5px;
}

QScrollBar::handle:vertical:hover {
    background-color: #465F82;
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
   USER CARD
   ========================================================== */

QLabel#userInfo {
    background-color: #101C2F;
    border: 1px solid #223650;
    border-radius: 10px;
    padding: 11px;
    color: #C8D3E1;
    font-size: 13px;
}
"""


def fix_scroll_surfaces(
    root: QWidget,
):
    """
    Qt ichidagi viewport/content widgetlar oq bo'lib
    qolmasligi uchun majburiy dark surface.
    """

    if root is None:
        return

    scroll_areas = root.findChildren(
        QScrollArea
    )

    for scroll in scroll_areas:
        scroll.setAutoFillBackground(
            True
        )

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

            QScrollArea > QWidget {
                background-color: #08111F;
            }

            QScrollArea > QWidget > QWidget {
                background-color: #08111F;
            }
            """
        )

        viewport = scroll.viewport()

        if viewport is not None:
            viewport.setStyleSheet(
                """
                background-color: #08111F;
                border: none;
                """
            )

        content = scroll.widget()

        if content is not None:
            content.setStyleSheet(
                content.styleSheet()
                + """
                background-color: #08111F;
                """
            )

    abstract_areas = root.findChildren(
        QAbstractScrollArea
    )

    for area in abstract_areas:
        viewport = area.viewport()

        if viewport is not None:
            viewport.setStyleSheet(
                viewport.styleSheet()
                + """
                background-color: #08111F;
                """
            )


def apply_premium_theme(
    root: QWidget,
):
    if root is None:
        return

    root.setStyleSheet(
        root.styleSheet()
        + PREMIUM_QSS
    )

    fix_scroll_surfaces(
        root
    )


class PremiumThemeEventFilter(
    QObject
):
    def eventFilter(
        self,
        watched,
        event,
    ):
        if event.type() in (
            QEvent.Type.Show,
            QEvent.Type.ShowToParent,
        ):
            if isinstance(
                watched,
                QWidget,
            ):
                QTimer.singleShot(
                    0,
                    lambda widget=watched:
                    fix_scroll_surfaces(
                        widget
                    ),
                )

        return False


_theme_filter = None


def install_premium_theme(
    root: QWidget,
):
    global _theme_filter

    apply_premium_theme(
        root
    )

    app = QApplication.instance()

    if app is None:
        return

    if _theme_filter is None:
        _theme_filter = (
            PremiumThemeEventFilter()
        )

        app.installEventFilter(
            _theme_filter
        )
