"""A native, keyboard-accessible radio button with a wrapping answer label."""
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QHBoxLayout, QLabel, QRadioButton, QSizePolicy,
                               QStyle, QStyleOptionButton, QStylePainter)


class AnswerRadioButton(QRadioButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setAccessibleName(text)
        self.answer_label = QLabel(text, self)
        self.answer_label.setObjectName('answerText')
        self.answer_label.setTextFormat(Qt.TextFormat.PlainText)
        self.answer_label.setWordWrap(True)
        self.answer_label.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.answer_label.setStyleSheet('background: transparent;')
        layout = QHBoxLayout(self)
        layout.setContentsMargins(32, 8, 12, 8)
        layout.addWidget(self.answer_label)
        policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        policy.setHeightForWidth(True)
        self.setSizePolicy(policy)

    def heightForWidth(self, width):
        return max(36, self.answer_label.heightForWidth(max(1, width - 44)) + 16)

    def sizeHint(self):
        return QSize(500, self.heightForWidth(500))

    def minimumSizeHint(self):
        return QSize(160, 36)

    def hitButton(self, position):
        return self.rect().contains(position)

    def paintEvent(self, event):
        painter = QStylePainter(self)
        option = QStyleOptionButton()
        self.initStyleOption(option)
        option.text = ''  # Child QLabel draws the wrapped text; native style draws indicator/focus.
        painter.drawControl(QStyle.ControlElement.CE_RadioButton, option)
