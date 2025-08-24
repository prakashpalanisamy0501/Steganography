import sys, hashlib, os
import winreg
from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QGridLayout, QSpacerItem, QSizePolicy, QApplication, QMessageBox, QInputDialog
from PyQt5.QtGui import QFont, QCursor, QIcon
from PyQt5.QtCore import Qt
from stego import SteganographyScreen
from button import CustomButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("STEGANOGRAPHY")
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.jpg")
        self.setWindowIcon(QIcon(icon_path))
        self.setFixedSize(1500, 800)
        self.setStyleSheet("background-color: #CCCCFF;")

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)

        label = QLabel("WELCOME TO STEGANOGRAPHY PROJECT")
        label.setFont(QFont("Arial", 26, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: #292966;")

        main_layout.addSpacerItem(QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding))
        main_layout.addWidget(label)
        main_layout.addSpacerItem(QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding))

        label2 = QLabel("SELECT THE TYPE OF STEGANOGRAPHY")
        label2.setFont(QFont("Arial", 20, QFont.Bold))
        label2.setAlignment(Qt.AlignCenter)
        label2.setStyleSheet("color: #4A4A99;")
        main_layout.addWidget(label2)

        self.text_screen  = SteganographyScreen("TEXT STEGANOGRAPHY", "TEXT STEGANOGRAPHY")
        self.image_screen = SteganographyScreen("IMAGE STEGANOGRAPHY", "IMAGE STEGANOGRAPHY")
        self.audio_screen = SteganographyScreen("AUDIO STEGANOGRAPHY", "AUDIO STEGANOGRAPHY")
        self.video_screen = SteganographyScreen("VIDEO STEGANOGRAPHY", "VIDEO STEGANOGRAPHY")

        button1 = CustomButton("Text Steganography", self.text_screen.show)
        button2 = CustomButton("Image Steganography", self.image_screen.show)
        button3 = CustomButton("Audio Steganography", self.audio_screen.show)
        button4 = CustomButton("Video Steganography", self.video_screen.show)

        button5= QPushButton("Back")
        button5.setFont(QFont("Arial", 14))
        button5.clicked.connect(self.gotoLoginPage)
        button5.setStyleSheet(f"""
            QPushButton {{
                width=130;
                height=40;
                background-color: {"#5C5C99"};
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
                background-color: {"#7878B8"};
            }}
            QPushButton:pressed {{
                background-color: {"#4252D6"};
            }}
        """)
        
        main_layout.addSpacerItem(QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding))

        main_layout.addWidget(button1, alignment=Qt.AlignCenter)
        main_layout.addWidget(button2, alignment=Qt.AlignCenter)
        main_layout.addWidget(button3, alignment=Qt.AlignCenter)
        main_layout.addWidget(button4, alignment=Qt.AlignCenter)
        
        main_layout.addSpacerItem(QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding))

        main_layout.addWidget(button5, alignment=Qt.AlignCenter)
        main_layout.addSpacerItem(QSpacerItem(100, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))  # Left gap

        self.setLayout(main_layout)
        
    def gotoLoginPage(self):
        self.hide() 
        self.login_window = LoginDialog()
        self.login_window.show()

class LoginDialog(QWidget):
    REG_PATH = r"SOFTWARE\MyApp"
    def __init__(self):
        super().__init__()
        
        stylesheet = """
            QLineEdit {
                background-color: #E6E6FF;
                color: #292966;
                border: 1px solid #4A4A99;
                border-radius: 5px;
                padding: 5px;
            }
            """

        app.setStyleSheet(stylesheet)

        self.setWindowTitle("Login")
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.jpg")
        self.setWindowIcon(QIcon(icon_path))
        self.setFixedSize(1500, 800)
        self.setStyleSheet("background-color: #CCCCFF")

        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.label = QLabel("Enter the Password")
        self.label.setFont(QFont("Arial", 16, QFont.Bold))
        self.label.setStyleSheet("color: #292966;")

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setReadOnly(False)
        self.password_input.setFixedSize(400, 50)
        self.password_input.setFont(QFont("Arial", 14))
        self.password_input.setPlaceholderText("Enter the password ")
        
        self.login_button = QPushButton("Login")
        self.login_button.setFont(QFont("Arial", 14))
        self.login_button.clicked.connect(self.check_password)
        self.style_button(self.login_button)

        self.change_password_button = QPushButton("Change Password")
        self.change_password_button.setFont(QFont("Arial", 14))
        self.change_password_button.clicked.connect(self.change_password)
        self.style_button(self.change_password_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.setFont(QFont("Arial", 14))
        self.exit_button.clicked.connect(self.exit)
        self.style_button(self.exit_button)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0, 1, 2, Qt.AlignCenter)
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding), 1, 0, 1, 2)

        encryption_file_layout1 = QHBoxLayout()
        encryption_file_layout1.addWidget(self.password_input)
        encryption_file_layout1.addWidget(self.login_button)
        encryption_file_layout1.setAlignment(Qt.AlignCenter)
        layout.addLayout(encryption_file_layout1, 2, 0, 1, 1, Qt.AlignCenter)
        
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding), 3, 0, 1, 2)

        encryption_file_layout2 = QHBoxLayout()
        encryption_file_layout2.addWidget(self.change_password_button)
        encryption_file_layout2.setAlignment(Qt.AlignCenter)
        layout.addLayout(encryption_file_layout2, 4, 0, 1, 1, Qt.AlignCenter)

        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding), 5, 0, 1, 2)

        encryption_file_layout3 = QHBoxLayout()
        encryption_file_layout3.addWidget(self.exit_button)
        encryption_file_layout3.setAlignment(Qt.AlignCenter)
        layout.addLayout(encryption_file_layout3, 6, 0, 1, 1, Qt.AlignCenter)
        
        main_layout.addLayout(layout)
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(main_layout)

        self.default_password = "admin123"
        self.default_hashed_password = self.hash_password(self.default_password)
        self.stored_hashed_password = self.load_password()

    def style_button(self, button):
        button.setStyleSheet("""
            QPushButton {
                background-color: #5C5C99;
                border-radius: 10px;
                border: none;
                color: #ffffff;
                font-size: 15px;
                font-weight: 500;
                padding: 14px 30px;
            }
            QPushButton:hover {
                background-color: #7878B8;
            }
            QPushButton:pressed {
                background-color: #4252D6;
            }
        """)
        button.setFixedSize(200, 50)

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def load_password(self):
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.REG_PATH, 0, winreg.KEY_READ) as key:
                stored_password, _ = winreg.QueryValueEx(key, "Password")
                return stored_password
        except FileNotFoundError:
            self.save_password(self.default_hashed_password)
            return self.default_hashed_password

    def save_password(self, hashed_password):
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, self.REG_PATH) as key:
            winreg.SetValueEx(key, "Password", 0, winreg.REG_SZ, hashed_password)

    def check_password(self):
        entered_password = self.password_input.text()
        entered_hashed = self.hash_password(entered_password)

        if entered_hashed == self.stored_hashed_password:
            self.accept_login()
        else:
            QMessageBox.critical(self, "Login Failed", "Incorrect password. Try again.")

    def accept_login(self):
        self.hide()
        self.main_window = MainWindow()
        self.main_window.show()
        
    def change_password(self):
        old_password, ok = QInputDialog.getText(self, "Verify Password", "Enter old password:", QLineEdit.Password)
        if not ok or self.hash_password(old_password) != self.stored_hashed_password:
            QMessageBox.critical(self, "Error", "Old password is incorrect!")
            return

        new_password, ok = QInputDialog.getText(self, "Change Password", "Enter new password:", QLineEdit.Password)
        if not ok or not new_password:
            QMessageBox.warning(self, "Error", "New password cannot be empty!")
            return

        new_hashed_password = self.hash_password(new_password)
        self.save_password(new_hashed_password)  
        self.stored_hashed_password = new_hashed_password

        QMessageBox.information(self, "Success", "Password changed successfully!")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.check_password()
            self.password_input.clear()
    
    def exit(self):
        confirm = QMessageBox.question(self, "Logout", "Are you sure you want to exit?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    login = LoginDialog()
    login.show()

    sys.exit(app.exec_())

