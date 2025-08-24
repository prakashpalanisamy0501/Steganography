from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont,QCursor
from PyQt5.QtCore import Qt

class CustomButton(QPushButton):
    def __init__(self, text, callback, width=250, height=80, color="#5C5C99", hover_color="#7878B8", pressed_color="#4252D6"):
        super().__init__(text)
        self.clicked.connect(callback)
        self.setFixedSize(width, height)

        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.setFont(font)

        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                border-radius: 10px;
                border: none;
                color: #ffffff;
                font-family: 'Inter', -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif;
                font-size: 15px;
                font-weight: 500;
                padding: 14px 30px;
                text-align: center;
                text-decoration: none;
                outline: none;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
            }}
            QPushButton:pressed {{
                background-color: {pressed_color};
            }}
        """)
        self.setCursor(QCursor(Qt.PointingHandCursor))

class StegoButton(QPushButton):
    def __init__(self, text, callback, width=130, height=40, color="#5C5C99", hover_color="#7878B8", pressed_color="#4252D6"):
        super().__init__(text)
        self.clicked.connect(callback)
        self.setFixedSize(width, height)

        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.setFont(font)

        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                border-radius: 10px;
                border: none;
                color: #ffffff;
                font-family: 'Inter', -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif;
                font-size: 15px;
                font-weight: 500;
                padding: 14px 30px;
                text-align: center;
                text-decoration: none;
                outline: none;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
            }}
            QPushButton:pressed {{
                background-color: {pressed_color};
            }}
        """)
        self.setCursor(QCursor(Qt.PointingHandCursor))
