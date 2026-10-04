"""Offline teaching figures. Optional media never controls lesson completion."""
from html import escape
import logging
from pathlib import Path

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QImageReader, QPainter, QPixmap
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtWidgets import (QBoxLayout, QDialog, QHBoxLayout, QLabel,
                              QPushButton, QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

from courses.visual_catalog import asset_path


def load_figure(filename):
    path = asset_path(filename)
    if path.suffix.lower() == '.svg':
        renderer = QSvgRenderer(str(path))
        if not renderer.isValid():
            return QPixmap()
        size = renderer.defaultSize()
        if size.isEmpty():
            return QPixmap()
        size.scale(QSize(1800, 1400), Qt.AspectRatioMode.KeepAspectRatio)
        image = QPixmap(size)
        image.fill(Qt.GlobalColor.transparent)
        painter = QPainter(image)
        renderer.render(painter)
        painter.end()
        return image
    reader = QImageReader(str(path))
    reader.setAutoTransform(True)
    return QPixmap.fromImage(reader.read())


class FigureDialog(QDialog):
    """Fit initially; explicit bounded zoom, scrolling and Escape close."""
    def __init__(self, pixmap, title, parent=None):
        super().__init__(parent)
        self.setObjectName('figureDialog')
        self.setWindowTitle(title)
        self.resize(1040, 740)
        self.original = pixmap
        self.zoom = 1.0
        layout = QVBoxLayout(self)
        bar = QHBoxLayout()
        for label, name, callback in (
            ('−', 'figureZoomOut', lambda: self.set_zoom(self.zoom / 1.25)),
            ('+', 'figureZoomIn', lambda: self.set_zoom(self.zoom * 1.25)),
            ('Oynaga moslash', 'figureFit', self.fit),
            ('Yopish', 'figureClose', self.close),
        ):
            button = QPushButton(label)
            button.setObjectName(name)
            button.clicked.connect(callback)
            bar.addWidget(button)
        layout.addLayout(bar)
        self.scroll = QScrollArea()
        self.scroll.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scroll.setWidget(self.label)
        layout.addWidget(self.scroll)
        self.fit()

    def fit(self):
        available = self.size() - QSize(70, 110)
        self.set_zoom(min(available.width() / self.original.width(),
                          available.height() / self.original.height()))

    def set_zoom(self, value):
        self.zoom = max(.1, min(4., value))
        size = self.original.size() * self.zoom
        scaled = self.original.scaled(size, Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        self.label.setPixmap(scaled)
        self.label.resize(scaled.size())


class LessonVisual(QWidget):
    def __init__(self, spec, reading_font_size=17, parent=None):
        super().__init__(parent)
        self.spec = spec
        self.setObjectName('lessonVisual')
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        self.layout = QBoxLayout(QBoxLayout.Direction.LeftToRight, self)
        self.layout.setContentsMargins(0, 8, 0, 8)
        self.layout.setSpacing(20)
        self.image_panel = QWidget()
        image_layout = QVBoxLayout(self.image_panel)
        image_layout.setContentsMargins(0, 0, 0, 0)
        image_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.image = QLabel()
        self.image.setObjectName('lessonFigure')
        self.image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image.setMinimumSize(1, 1)
        self.image.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Fixed)
        try:
            self.original = load_figure(spec['asset'])
        except Exception:
            logging.exception('Optional lesson figure could not be loaded')
            self.original = QPixmap()
        image_layout.addWidget(self.image)
        self.enlarge = QPushButton('KATTALASHTIRISH')
        self.enlarge.setObjectName('enlargeLessonFigure')
        self.enlarge.setMinimumHeight(36)
        self.enlarge.setStyleSheet('QPushButton {color: #0E5558; background: #FFFDF7; '
                                   'border: 1px solid #0E5558; border-radius: 5px; '
                                   'padding: 6px 16px; font-size: 13px;} '
                                   'QPushButton:disabled {color: #697571; border-color: #697571;}')
        self.enlarge.setEnabled(not self.original.isNull())
        self.enlarge.clicked.connect(self.open_figure)
        image_layout.addWidget(self.enlarge, alignment=Qt.AlignmentFlag.AlignCenter)
        self.details = QLabel()
        self.details.setObjectName('figureExplanation')
        self.details.setWordWrap(True)
        self.details.setTextFormat(Qt.TextFormat.RichText)
        self.details.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse |
                                            Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.details.setOpenExternalLinks(True)
        paragraphs = ''.join('<p>' + escape(item) + '</p>' for item in spec['explanation'])
        source = spec.get('source_url')
        credit = escape(spec.get('credit', 'ARCHIPRO UZ — o‘quv chizmasi'))
        if source:
            credit = '<a href="' + escape(source, quote=True) + '">' + credit + '</a>'
        html = (f'<div style="font-family: Segoe UI; font-size: {reading_font_size}px; color: #203B36;">'
                f'<b>{escape(spec["title"])}</b>{paragraphs}'
                f'<p><b>Mashq:</b> {escape(spec["exercise"])}</p>'
                f'<p><b>Yechim:</b> {escape(spec["solution"])}</p>'
                f'<p>{escape(spec["boundary"])}</p><p>{credit}</p></div>')
        self.details.setProperty('readingHtml', html)
        self.details.setText(html)
        self.layout.addWidget(self.image_panel, 3)
        self.layout.addWidget(self.details, 2)
        self.dialog = None
        if self.original.isNull():
            self.image.setText('Chizma ochilmadi. Dars matni va testdan foydalanishingiz mumkin.')
            self.image.setWordWrap(True)
            self.image.setFixedHeight(95)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.layout.setDirection(QBoxLayout.Direction.TopToBottom if self.width() < 900
                                 else QBoxLayout.Direction.LeftToRight)
        if not self.original.isNull():
            available = min(880, max(120, self.image_panel.width()))
            target = QSize(available, 520)
            pixmap = self.original.scaled(target, Qt.AspectRatioMode.KeepAspectRatio,
                                          Qt.TransformationMode.SmoothTransformation)
            self.image.setPixmap(pixmap)
            self.image.setFixedHeight(pixmap.height())

    def open_figure(self):
        if self.original.isNull():
            return
        if self.dialog is None:
            self.dialog = FigureDialog(self.original, self.spec['title'], self)
        self.dialog.show()
        self.dialog.raise_()
        self.dialog.activateWindow()
