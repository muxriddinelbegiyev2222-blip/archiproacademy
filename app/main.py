import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ARCHIPRO UZ")
        self.resize(1280, 720)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)

        title = QLabel("ARCHIPRO UZ")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(
            """
            QLabel {
                font-size: 42px;
                font-weight: 700;
                color: #F5F7FA;
            }
            """
        )

        subtitle = QLabel(
            "0 dan PRO darajagacha\n"
            "Arxitektura va Archicad Professional Academy"
        )
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet(
            """
            QLabel {
                font-size: 18px;
                color: #AAB3C2;
                line-height: 1.5;
            }
            """
        )

        start_button = QPushButton("BOSHLASH")
        start_button.setFixedSize(220, 52)
        start_button.setCursor(Qt.CursorShape.PointingHandCursor)
        start_button.setStyleSheet(
            """
            QPushButton {
                background-color: #2F80ED;
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 16px;
                font-weight: 600;
            }

            QPushButton:hover {
                background-color: #3B8EF3;
            }

            QPushButton:pressed {
                background-color: #246CC4;
            }
            """
        )

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(20)
        layout.addWidget(start_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #111827;
            }
            """
        )


def main():
    app = QApplication(sys.argv)

    app.setApplicationName("ARCHIPRO UZ")
    app.setOrganizationName("ARCHIPRO UZ")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
