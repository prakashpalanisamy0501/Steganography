import numpy as np
import os, cv2, wave
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QPushButton, QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QGridLayout, QMessageBox
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from button import StegoButton

class SteganographyScreen(QWidget):
    def __init__(self, title, message):
        super().__init__()
        self.setWindowTitle(title)
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.jpg")
        self.setWindowIcon(QIcon(icon_path))
        self.setFixedSize(1300, 700)
        self.setStyleSheet("background-color: #CCCCFF;")

        self.selected_encrypt_file_name= None
        self.user_input= None
        self.selected_decrypt_file_path= None
        self.encrypted_frame=None
        
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        
        label = QLabel(message)
        label.setFont(QFont("Arial", 18, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: #292966;")

        label2 = QLabel("ENCRYPTION")
        label2.setFont(QFont("Arial", 18, QFont.Bold))
        label2.setAlignment(Qt.AlignLeft)
        label2.setStyleSheet("color: #4A4A99;")
        
        label3 = QLabel("DECRYPTION")
        label3.setFont(QFont("Arial", 18, QFont.Bold))
        label3.setAlignment(Qt.AlignLeft)
        label3.setStyleSheet("color: #4A4A99;")

        font = QFont()
        font.setPointSize(10)
        
        button_style = """
        QPushButton {
            background-color: #4A4A99;
            color: white;
            border: 2px solid #292966;
            border-radius: 5px;
            padding: 6px 12px;
        }

        QPushButton:hover {
            background-color: #6666CC;
        }

        QPushButton:pressed {
            background-color: #2E2E80;
        }
        """
        self.encryption_file_input = QLineEdit()
        self.encryption_file_input.setPlaceholderText("Select file for encryption...")
        self.encryption_file_input.setReadOnly(True)
        self.encryption_file_input.setFont(font)
        self.encryption_file_input.setFixedSize(500, 40)
        
        encrypt_file_select_methods = {
            "TEXT STEGANOGRAPHY": self.select_encrypt_text_file,
            "IMAGE STEGANOGRAPHY": self.select_encrypt_image_file,
            "AUDIO STEGANOGRAPHY": self.select_encrypt_audio_file,
            "VIDEO STEGANOGRAPHY": self.select_encrypt_video_file,
        }

        encrypt_file_select_method = encrypt_file_select_methods.get(message)
        if encrypt_file_select_method:
            self.encryption_file_select_button = StegoButton("Select File", encrypt_file_select_method)
            
        self.encryption_text_input = QLineEdit()
        self.encryption_text_input.setPlaceholderText("Enter the Text to Encrypt...")
        self.encryption_text_input.setReadOnly(False)   
        self.encryption_text_input.setFixedSize(630, 50)
        self.encryption_text_input.setFont(font)

        self.encryption_password = QLineEdit()
        self.encryption_password.setPlaceholderText("Enter the password to protect the file...")
        self.encryption_password.setReadOnly(False)  
        self.encryption_password.setFixedSize(630, 50)
        self.encryption_password.setFont(font)

        self.file_name_with_extension = QLineEdit()
        self.file_name_with_extension.setPlaceholderText("Enter the name of the file after Encoding...")
        self.file_name_with_extension.setReadOnly(False) 
        self.file_name_with_extension.setFixedSize(630, 50)
        self.file_name_with_extension.setFont(font)

        self.encryption_button = QPushButton("Encrypt")
        self.encryption_button.setStyleSheet(button_style)
        self.encryption_button.setFixedSize(160, 50)  

        encrypt_file_methods = {
            "TEXT STEGANOGRAPHY": self.encode_txt_data,
            "IMAGE STEGANOGRAPHY": self.encode_img_data,
            "AUDIO STEGANOGRAPHY": self.encode_aud_data,
            "VIDEO STEGANOGRAPHY": self.encode_vid_data,
        }
        encrypt_method = encrypt_file_methods.get(message)
        if encrypt_method:
            self.encryption_button.clicked.connect(encrypt_method)

        self.password_to_decryption = QLineEdit()
        self.password_to_decryption.setPlaceholderText("Enter the password to decrypt the file... ")
        self.password_to_decryption.setReadOnly(False) 
        self.password_to_decryption.setFixedSize(630, 50)
        self.password_to_decryption.setFont(font)

        self.decryption_file_input = QLineEdit()
        self.decryption_file_input.setPlaceholderText("Select file for decryption...")
        self.decryption_file_input.setReadOnly(True)  
        self.decryption_file_input.setFont(font)
        self.decryption_file_input.setFixedSize(500, 40)

        decrypt_file_select_methods = {
            "TEXT STEGANOGRAPHY": self.select_decrypt_text_file,
            "IMAGE STEGANOGRAPHY": self.select_decrypt_image_file,
            "AUDIO STEGANOGRAPHY": self.select_decrypt_audio_file,
            "VIDEO STEGANOGRAPHY": self.select_decrypt_video_file,
        }

        decrypt_file_select_method = decrypt_file_select_methods.get(message)
        if decrypt_file_select_method:
            self.decryption_file_select_button = StegoButton("Select File", decrypt_file_select_method)
        
        self.decryption_button = QPushButton("Decrypt")
        self.decryption_button.setFixedSize(160, 50)  
        self.decryption_button.setStyleSheet(button_style)

        decrypt_file_methods = {
            "TEXT STEGANOGRAPHY": self.decode_txt_data,
            "IMAGE STEGANOGRAPHY": self.decode_img_data,
            "AUDIO STEGANOGRAPHY": self.decode_aud_data,
            "VIDEO STEGANOGRAPHY": self.decode_vid_data,
        }
        decrypt_method = decrypt_file_methods.get(message)
        if decrypt_method:
            self.decryption_button.clicked.connect(decrypt_method) 
            
        layout = QGridLayout()
        layout.addWidget(label, 0, 0, 1, 2, Qt.AlignCenter) 
        layout.addWidget(label2, 1, 0, 1, 2, Qt.AlignLeft) 

        encryption_file_layout1 = QHBoxLayout()
        encryption_file_layout1.addWidget(self.encryption_text_input)
        encryption_file_layout1.setAlignment(Qt.AlignCenter)
        layout.addLayout(encryption_file_layout1, 2, 0, 1, 1, Qt.AlignCenter)

        encryption_file_layout2 = QHBoxLayout()
        encryption_file_layout2.addWidget(self.encryption_password)
        encryption_file_layout2.setAlignment(Qt.AlignCenter)
        layout.addLayout(encryption_file_layout2, 3, 0, 1, 1, Qt.AlignCenter)

        encryption_file_layout3 = QHBoxLayout()
        encryption_file_layout3.addWidget(self.file_name_with_extension)
        encryption_file_layout3.setAlignment(Qt.AlignCenter)
        layout.addLayout(encryption_file_layout3, 4, 0, 1, 1, Qt.AlignCenter)

        encryption_file_layout4 = QHBoxLayout()
        encryption_file_layout4.addWidget(self.encryption_file_input)
        encryption_file_layout4.addWidget(self.encryption_file_select_button)
        encryption_file_layout4.setAlignment(Qt.AlignCenter)  

        layout.addLayout(encryption_file_layout4, 5, 0, 1, 2, Qt.AlignCenter)

        encryption_file_layout5=QHBoxLayout()
        encryption_file_layout5.addWidget(self.encryption_button)
        encryption_file_layout5.setAlignment(Qt.AlignCenter)
        layout.addLayout(encryption_file_layout5, 6, 0, 1, 1, Qt.AlignCenter)

        layout.addWidget(label3, 7, 0, 1, 2, Qt.AlignLeft) 

        decryption_file_layout1=QHBoxLayout()
        decryption_file_layout1.addWidget(self.password_to_decryption)
        decryption_file_layout1.setAlignment(Qt.AlignCenter)
        layout.addLayout(decryption_file_layout1, 8, 0, 1, 1, Qt.AlignCenter)

        decryption_file_layout1 = QHBoxLayout()
        decryption_file_layout1.addWidget(self.decryption_file_input)
        decryption_file_layout1.addWidget(self.decryption_file_select_button)
        decryption_file_layout1.setAlignment(Qt.AlignCenter)  

        layout.addLayout(decryption_file_layout1, 9, 0, 1, 2, Qt.AlignCenter) 

        decryption_file_layout3=QHBoxLayout()
        decryption_file_layout3.addWidget(self.decryption_button)
        decryption_file_layout3.setAlignment(Qt.AlignCenter)
        layout.addLayout(decryption_file_layout3, 10, 0, 1, 1, Qt.AlignCenter)
      
        self.setLayout(layout) 

    def select_encrypt_text_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Text File", "", "Text Files (*.txt)")
        if file_name:
            self.encryption_file_input.setText(file_name)
            self.selected_encrypt_file_path = file_name 
    
    def encode_txt_data(self):
        user_text_input=self.encryption_text_input.text().strip() 
        password = self.encryption_password.text().strip()
        base_name = self.file_name_with_extension.text().strip()
        
        if not user_text_input:
            QMessageBox.warning(self, "Error", "Enter the message to encrypt")
            return

        if not password:
            QMessageBox.warning(self, "Error", "Enter the password to protect the your message")
            return

        if not base_name:
            QMessageBox.warning(self, "Error", "Enter the file name with extension")
            return
        base_name=base_name + ".txt"

        if not hasattr(self, 'selected_encrypt_file_path') or not self.selected_encrypt_file_path:
            QMessageBox.warning(self, "Error", "No file selected!")
            return
        
        input_file= self.selected_encrypt_file_path

        count2=0
        with open(input_file, "r", encoding="utf-8") as file1:
            for line in file1: 
                for word in line.split():
                    count2=count2+1     
        bt=int(count2)

        max_word_capacity = bt // 6

        if len(user_text_input) > max_word_capacity:
            QMessageBox.warning(self, "Encryption Error", "String is too big. Please reduce the string size.")
            return

        encrypted_text = self.encryption(user_text_input, password)
        encrypted_text += '*^*^*'  
        self.txt_encode(input_file, encrypted_text, base_name)

        QMessageBox.information(self, "Text Encryption", "Text file has been encrypted successfully")
        self.encryption_file_input.clear()
        self.encryption_password.clear()
        self.encryption_text_input.clear()
        self.file_name_with_extension.clear()

    def txt_encode(self, file_name, text, base_name):
        l = len(text)
        i = 0
        add = ''

        while i < l:
            t = ord(text[i]) 
            if 0 <= t <= 64:
                t1 = t + 48
                t2 = t1 ^ 170 
                res = bin(t2)[2:].zfill(8)
                add += "0011" + res 
            else:
                t1 = t - 48
                t2 = t1 ^ 170
                res = bin(t2)[2:].zfill(8)
                add += "0110" + res
                
            i += 1

        res1 = ''.join(filter(lambda x: x in '01', add)) + "111111111111"
       
        encrypted_folder = os.path.join(os.getcwd(), "encrypted_files")
        if not os.path.exists(encrypted_folder):
            os.makedirs(encrypted_folder)

        nameoffile = os.path.join(encrypted_folder, base_name)
        HM_SK = ""
        ZWC = {"00": u'\u200C', "01": u'\u202C', "11": u'\u202D', "10": u'\u200E'}

        with open(file_name, "r+", encoding="utf-8") as file1:
            words = [word for line in file1 for word in line.split()]

        required_words = len(res1) // 12
        if len(words) < required_words:
            QMessageBox.warning(self, "Error", "Text file is too short for encoding!")
            return

        with open(nameoffile, "w+", encoding="utf-8") as file3:
            i = 0
            while i < len(res1):  
                s = words[i // 12]
                j = 0
                x = ""
                HM_SK = ""
                while j < 12:
                    x = res1[j + i] + res1[i + j + 1]
                    HM_SK += ZWC[x]
                    j += 2
                s1 = s + HM_SK
                file3.write(s1 + " ")
                i += 12

            for t in range(len(res1) // 12, len(words)): 
                file3.write(words[t] + " ")

    def select_encrypt_image_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", "Image Files (*.png;*.jpg;)")
        if file_name:
            self.encryption_file_input.setText(file_name)
            self.selected_encrypt_file_path = file_name 
    
    @staticmethod 
    def msgtobinary(data):
        if isinstance(data, str):
            result= ''.join(format(ord(char), '08b') for char in data)
        elif isinstance(data, (int, np.uint8)):
            result= format(int(data), '08b')
        elif isinstance(data, np.ndarray):  
            result= [format(int(val), '08b') for val in data]
        else:
            result= TypeError(f"Unsupported data type: {type(data)}")
        return result

    def encode_img_data(self):
        user_text_input = self.encryption_text_input.text().strip() 
        password = self.encryption_password.text().strip()
        base_name = self.file_name_with_extension.text().strip()

        if not user_text_input:
            QMessageBox.warning(self, "Error", "Enter the message to encrypt")
            return

        if not password:
            QMessageBox.warning(self, "Error", "Enter the password to protect your message")
            return

        if not base_name:
            QMessageBox.warning(self, "Error", "Enter the file name with extension")
            return
        base_name=base_name + ".png"

        if not hasattr(self, 'selected_encrypt_file_path') or not self.selected_encrypt_file_path:
            QMessageBox.warning(self, "Error", "No file selected!")
            return

        img = cv2.imread(self.selected_encrypt_file_path)
        if img is None:
            QMessageBox.warning(self, "Error", "Image could not be loaded. Please check the file path.")
            return

        no_of_bytes=(img.shape[0] * img.shape[1] * 3) // 8
        if len(user_text_input) > no_of_bytes:
            QMessageBox.warning(self, "Error", f"Insufficient space in the image! Use a larger image or provide less data! No_of_bytes: {no_of_bytes}")
            return
        
        encrypted_folder = os.path.join(os.getcwd(), "encrypted_files")
        if not os.path.exists(encrypted_folder):
            os.makedirs(encrypted_folder)
        nameoffile = os.path.join(encrypted_folder, base_name)

        ciphertext = self.encryption(user_text_input, password)
        data_to_hide = ciphertext + '*^*^*'
        binary_message = self.msgtobinary(data_to_hide)
        message_length = len(binary_message)
        
        index_data = 0
        for row in img:
            for pixel in row:
                r, g, b = self.msgtobinary(int(pixel[0])), self.msgtobinary(int(pixel[1])), self.msgtobinary(int(pixel[2]))
                if index_data < message_length:
                    pixel[0] = int(r[:-1] + binary_message[index_data], 2)
                    index_data += 1
                if index_data < message_length:
                    pixel[1] = int(g[:-1] + binary_message[index_data], 2)
                    index_data += 1
                if index_data < message_length:
                    pixel[2] = int(b[:-1] + binary_message[index_data], 2)
                    index_data += 1
                if index_data >= message_length:
                    break
        success=cv2.imwrite(nameoffile, img)
        if success:
            QMessageBox.information(self, "Image Encryption", "Image file has been encrypted successfully")
            self.encryption_file_input.clear()
            self.encryption_text_input.clear()
            self.encryption_password.clear()
            self.file_name_with_extension.clear()
        else:
            QMessageBox.warning(self, "Error", "Failed to save the encrypted image!")
            self.encryption_file_input.clear()
            self.encryption_text_input.clear()
            self.encryption_password.clear()
            self.file_name_with_extension.clear()

    def select_encrypt_audio_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Audio File", "", "Audio Files (*.wav;)")
        if file_name:
            self.encryption_file_input.setText(file_name) 
            self.selected_encrypt_file_path = file_name 

    def encode_aud_data(self):
        data = self.encryption_text_input.text().strip() 
        password = self.encryption_password.text().strip()
        base_name = self.file_name_with_extension.text().strip()

        if not data:
            QMessageBox.warning(self, "Error", "Enter the message to encrypt")
            return

        if not password:
            QMessageBox.warning(self, "Error", "Enter the password to protect your message")
            return

        if not base_name:
            QMessageBox.warning(self, "Error", "Enter the file name with extension")
            return
        base_name=base_name + ".wav"

        if not hasattr(self, 'selected_encrypt_file_path') or not self.selected_encrypt_file_path:
            QMessageBox.warning(self, "Error", "No file selected!")
            return

        nameoffile= self.selected_encrypt_file_path

        song = wave.open(nameoffile, mode='rb')
        if song is None:
            QMessageBox.warning(self, "Error", "Audio could not be loaded. Please check the file path.")
            return

        nframes=song.getnframes()
        frames=song.readframes(nframes)
        frame_list=list(frames)
        frame_bytes=bytearray(frame_list)

        encrypted_data = self.encryption(data, password)

        res = ''.join(format(i, '08b') for i in bytearray(encrypted_data, encoding ='utf-8'))     

        encrypted_data = encrypted_data + '*^*^*'

        result = []
        for c in encrypted_data:
            bits = bin(ord(c))[2:].zfill(8)
            result.extend([int(b) for b in bits])

        j = 0
        for i in range(0,len(result),1): 
            res = bin(frame_bytes[j])[2:].zfill(8)
            if res[len(res)-4]== result[i]:
                frame_bytes[j] = (frame_bytes[j] & 253)      
            else:
                frame_bytes[j] = (frame_bytes[j] & 253) | 2
                frame_bytes[j] = (frame_bytes[j] & 254) | result[i]
            j = j + 1
        
        frame_modified = bytes(frame_bytes)
        
        encrypted_folder = os.path.join(os.getcwd(), "encrypted_files")
        if not os.path.exists(encrypted_folder):
            os.makedirs(encrypted_folder)
        stegofile = os.path.join(encrypted_folder, base_name)

        with wave.open(stegofile, 'wb') as fd:
            fd.setparams(song.getparams())
            fd.writeframes(frame_modified)  
        song.close()

        QMessageBox.information(self, "Audio Encryption", "Audio file has been encrypted successfully")
        self.encryption_file_input.clear()
        self.encryption_text_input.clear()
        self.encryption_password.clear()
        self.file_name_with_extension.clear()

    def select_encrypt_video_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Video File", "", "Video Files (*.mp4; *.avi)")
        if file_name:
            self.encryption_file_input.setText(file_name)
            self.selected_encrypt_file_path = file_name
  
    @staticmethod
    def KSA(key):
        key_length = len(key)
        S=list(range(256)) 
        j=0
        for i in range(256):
            j=(j+S[i]+key[i % key_length]) % 256
            S[i],S[j]=S[j],S[i]
        return S
   
    @staticmethod
    def PRGA(S,n):
        i=0
        j=0
        key=[]
        while n>0:
            n=n-1
            i=(i+1)%256
            j=(j+S[i])%256
            S[i],S[j]=S[j],S[i]
            K=S[(S[i]+S[j])%256]
            key.append(K)
        return key
    
    @staticmethod
    def preparing_key_array(s):
        return [ord(c) for c in s]
    
    def encryption(self, plaintext, password):
        key = password
        key=self.preparing_key_array(key)
        
        S=self.KSA(key)

        keystream=np.array(self.PRGA(S,len(plaintext)), dtype=np.uint8)
        plaintext=np.array([ord(i) for i in plaintext], dtype=np.uint8)

        cipher=keystream^plaintext
        ctext = ''.join(chr(c) for c in cipher)
        return ctext
    
    def embed(self, frame, data, key):
        data=self.encryption(data, key)

        data +='*^*^*'
        binary_data=self.msgtobinary(data)
        length_data = len(binary_data)
        
        index_data = 0
        
        for row in frame:
            for pixel in row:
                r, g, b = self.msgtobinary(int(pixel[0])), self.msgtobinary(int(pixel[1])), self.msgtobinary(int(pixel[2]))
                if index_data < length_data:
                    pixel[0] = int(r[:-1] + binary_data[index_data], 2) 
                    index_data += 1
                if index_data < length_data:
                    pixel[1] = int(g[:-1] + binary_data[index_data], 2) 
                    index_data += 1
                if index_data < length_data:
                    pixel[2] = int(b[:-1] + binary_data[index_data], 2) 
                    index_data += 1
                if index_data >= length_data:
                    break
            return frame

    def encode_vid_data(self):
        data = self.encryption_text_input.text().strip() 
        password = self.encryption_password.text().strip()
        base_name = self.file_name_with_extension.text().strip()

        if not data:
            QMessageBox.warning(self, "Error", "Enter the message to encrypt")
            return

        if not password:
            QMessageBox.warning(self, "Error", "Enter the password to protect your message")
            return

        if not base_name:
            QMessageBox.warning(self, "Error", "Enter the file name with extension")
            return
        base_name=base_name + ".avi"

        if not hasattr(self, 'selected_encrypt_file_path') or not self.selected_encrypt_file_path:
            QMessageBox.warning(self, "Error", "No file selected!")
            return

        cap = cv2.VideoCapture(self.selected_encrypt_file_path)

        if cap is None:
            QMessageBox.warning(self, "Error", "Video could not be loaded. Please check the file path.")
            return

        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'FFV1')

        encrypted_folder = os.path.join(os.getcwd(), "encrypted_files")
        if not os.path.exists(encrypted_folder):
            os.makedirs(encrypted_folder)
        stegofile = os.path.join(encrypted_folder, base_name)

        out = cv2.VideoWriter(stegofile, fourcc, fps, (frame_width,frame_height))
        
        n = 1
        frame_number = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame_number += 1
            if frame_number == n:
                frame = self.embed(frame, data, password)
            out.write(frame)
        cap.release()
        out.release()
        
        QMessageBox.information(self, "Video Encryption", "Video file has been encrypted successfully")
        self.encryption_file_input.clear()
        self.encryption_text_input.clear()
        self.encryption_password.clear()
        self.file_name_with_extension.clear()
        
    def select_decrypt_text_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Text File", "", "Text Files (*.txt)")
        if file_name:
            self.decryption_file_input.setText(file_name)
            self.selected_decrypt_file_path = file_name 
            
    @staticmethod
    def BinaryToDecimal(binary):
        return int(binary, 2)

    def decode_txt_data(self):
        ZWC_reverse = {u'\u200C': "00", u'\u202C': "01", u'\u202D': "11", u'\u200E': "10"}
        
        password = self.password_to_decryption.text().strip()
        if not password:
            QMessageBox.warning(self, "Decryption Error", "Please enter a password.")
            return

        if not hasattr(self, 'selected_decrypt_file_path') or not self.selected_decrypt_file_path:
            QMessageBox.warning(self, "Error", "No file selected!")
            return

        stego = self.selected_decrypt_file_path
        temp = ""

        with open(stego, "r", encoding="utf-8") as file4:
            for line in file4: 
                for words in line.split():
                    binary_extract = ""
                    for letter in words:
                        if letter in ZWC_reverse:
                            binary_extract += ZWC_reverse[letter]
                    temp += binary_extract
      
        if "111111111111" in temp:
            temp = temp.split("111111111111")[0]
        else:
            QMessageBox.warning(self, "Decryption Error", "No valid hidden data found.")
            return

        if len(temp) % 12 != 0:
            QMessageBox.warning(self, "Decryption Error", "Corrupted data: incorrect binary length.")
            return

        final = ""
        for i in range(0, len(temp), 12):
            t3 = temp[i:i+4]  
            t4 = temp[i+4:i+12] 
            decimal_data = self.BinaryToDecimal(t4)
            if t3 == "0110":
                final += chr((decimal_data ^ 170) + 48)
            elif t3 == "0011":
                final += chr((decimal_data ^ 170) - 48)

        if "*^*^*" not in final:
            QMessageBox.warning(self, "Decryption Error", "No hidden data found.")
            self.password_to_decryption.clear()
            self.decryption_file_input.clear()
            return

        decoded_text = final.replace("*^*^*", "")

        try:
            final_decoded_msg = self.decryption(decoded_text, password)
            if not final_decoded_msg:
                QMessageBox.critical(self, "Error", "Decryption failed")
                self.password_to_decryption.clear()
                self.decryption_file_input.clear()
                return
        except Exception as e:
            QMessageBox.critical(self, "Decryption Error", f"Incorrect password or corrupted data.\nError: {e}")
            self.password_to_decryption.clear()
            self.decryption_file_input.clear()
            return

        if not final_decoded_msg.isprintable():  
            QMessageBox.critical(self, "Decryption Error", "Incorrect password. Please try again.")
            self.password_to_decryption.clear()
            self.decryption_file_input.clear()
            return

        QMessageBox.information(self, "Decryption Successful", f"The text has been successfully decrypted. The hidden data is:\n\n{final_decoded_msg} ")
        self.password_to_decryption.clear()
        self.decryption_file_input.clear()

    def select_decrypt_image_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", "Image Files (*.png)")
        if file_name:
            self.decryption_file_input.setText(file_name) 
            self.selected_decrypt_file_path = file_name 

    def decode_img_data(self):
        if not hasattr(self, 'selected_decrypt_file_path') or not self.selected_decrypt_file_path:
            QMessageBox.warning(self, "Error", "No file selected!")
            return

        password = self.password_to_decryption.text().strip()
        if not password:
            QMessageBox.warning(self, "Decryption Error", "Please enter a password.")
            return

        img = cv2.imread(self.selected_decrypt_file_path)
        if img is None:
            QMessageBox.warning(self, "Error", "Image could not be loaded. Please check the file path.")
            return

        data_binary = ""
        for row in img:
            for pixel in row:
                r, g, b = self.msgtobinary(pixel[0]), self.msgtobinary(pixel[1]), self.msgtobinary(pixel[2])
                data_binary += r[-1]  
                data_binary += g[-1]  
                data_binary += b[-1]

        total_bytes = [data_binary[i: i + 8] for i in range(0, len(data_binary), 8)]
        decoded_data = ""
        final_decoded_msg=""
        for byte in total_bytes:
            decoded_data += chr(int(byte, 2))
            if decoded_data[-5:] == '*^*^*':
                break
        
        if '*^*^' not in decoded_data:
            QMessageBox.critical(self, "Error", "No hidden data found")
            self.password_to_decryption.clear()
            self.decryption_file_input.clear()
            return
        
        final_decoded_msg = decoded_data.replace("*^*^*", "")
        try:
            final_decoded_msg = self.decryption(final_decoded_msg, password)
            if not final_decoded_msg:
               QMessageBox.critical(self, "Error", "Decryption failed")
               self.password_to_decryption.clear()
               self.decryption_file_input.clear()
               return
        except Exception:
            QMessageBox.critical(self, "Decryption Error", "Incorrect password or corrupted data.")
            self.password_to_decryption.clear()
            self.decryption_file_input.clear()
            return
        
        if not final_decoded_msg.isprintable():  
            QMessageBox.critical(self, "Decryption Error", "Incorrect password. Please try again.")
            self.password_to_decryption.clear()
            self.decryption_file_input.clear()
            return
        
        QMessageBox.information(self, "Decryption Successful", f"The text has been successfully decrypted:\n\n{final_decoded_msg}")
        self.password_to_decryption.clear()
        self.decryption_file_input.clear()
            
    def select_decrypt_audio_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Audio File", "", "Audio Files (*.wav)")
        if file_name:
            self.decryption_file_input.setText(file_name) 
            self.selected_decrypt_file_path = file_name

    def decode_aud_data(self):

        nameoffile=self.selected_decrypt_file_path
        password=self.password_to_decryption.text().strip()

        song = wave.open(nameoffile, mode='rb')
        if song is None:
            QMessageBox.warning(self, "Error", "Image could not be loaded. Please check the file path.")
            return
        
        nframes=song.getnframes()
        frames=song.readframes(nframes)
        frame_list=list(frames)
        frame_bytes=bytearray(frame_list)

        extracted = ""
        p=0
        for i in range(len(frame_bytes)):
            if(p==1):
                break
            res = bin(frame_bytes[i])[2:].zfill(8)
            if res[len(res)-2]==0:
                extracted+=res[len(res)-4]
            else:
                extracted+=res[len(res)-1]
        
        all_bytes = [ extracted[i: i+8] for i in range(0, len(extracted), 8) ]
        decoded_data = ""
        final_decoded_msg=""
        for byte in all_bytes:
            decoded_data += chr(int(byte, 2))
            if decoded_data[-5:] == "*^*^*":
                break

        if '*^*^' not in decoded_data:
            QMessageBox.critical(self, "Error", "No hidden data found")
            self.password_to_decryption.clear()
            self.decryption_file_input.clear()
            return
        
        final_decoded_msg = decoded_data.replace("*^*^*", "")

        try:
            final_decoded_msg=self.decryption(final_decoded_msg, password)
            if not final_decoded_msg:
               QMessageBox.critical(self, "Error", "Decryption failed")
               self.password_to_decryption.clear()
               self.decryption_file_input.clear()
               return
        except Exception:
            QMessageBox.critical(self, "Decryption Error", "Incorrect password or corrupted data.")
            self.password_to_decryption.clear()
            self.decryption_file_input.clear()
            return
        
        if not final_decoded_msg.isprintable(): 
            QMessageBox.critical(self, "Decryption Error", "Incorrect password. Please try again.")
            self.password_to_decryption.clear()
            self.decryption_file_input.clear()
            return

        QMessageBox.information(self, "Decryption Successful", f"The text has been successfully decrypted. The hidden data is:\n\n{final_decoded_msg} ")
        self.password_to_decryption.clear()
        self.decryption_file_input.clear()

    def select_decrypt_video_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Video File", "", "Video Files (*.avi)")
        if file_name:
            self.decryption_file_input.setText(file_name)
            self.selected_decrypt_file_path = file_name

    def decryption(self, ciphertext, password):
        key = self.preparing_key_array(password)
        S = self.KSA(key)
        keystream = np.array(self.PRGA(S, len(ciphertext)), dtype=np.uint8)
        ciphertext = np.array([ord(i) for i in ciphertext], dtype=np.uint8)

        decoded = keystream ^ ciphertext
        dtext = ''.join(chr(c) for c in decoded)

        return dtext

    def extract(self, frame, password):
        data_binary = ""
        final_decoded_msg = ""
        for row in frame:
            for pixel in row:
                r, g, b = self.msgtobinary(pixel[0]), self.msgtobinary(pixel[1]), self.msgtobinary(pixel[2])
                data_binary += r[-1]  
                data_binary += g[-1]  
                data_binary += b[-1]  
        total_bytes = [ data_binary[i: i+8] for i in range(0, len(data_binary), 8) ]
        decoded_data = ""
        for byte in total_bytes:
            decoded_data += chr(int(byte, 2))
            if decoded_data[-5:] == "*^*^*": 
                break
        if '*^*^' not in decoded_data:
            QMessageBox.critical(self, "Error", "No hidden data found")
            self.password_to_decryption.clear()
            self.decryption_file_input.clear()
            return

        final_decoded_msg = decoded_data.replace("*^*^*", "")

        try:
            final_decoded_msg=self.decryption(final_decoded_msg, password)
            if not final_decoded_msg:
               QMessageBox.critical(self, "Error", "Decryption failed")
               self.password_to_decryption.clear()
               self.decryption_file_input.clear()
               return
        except Exception:
            QMessageBox.critical(self, "Decryption Error", "Incorrect password or corrupted data.")
            self.password_to_decryption.clear()
            self.decryption_file_input.clear()
            return
        
        if not final_decoded_msg.isprintable():  
            QMessageBox.critical(self, "Decryption Error", "Incorrect password. Please try again.")
            self.password_to_decryption.clear()
            self.decryption_file_input.clear()
            return

        QMessageBox.information(self, "Decryption Successful", f"The text has been successfully decrypted. The hidden data is:\n\n{final_decoded_msg} ")
        self.password_to_decryption.clear()
        self.decryption_file_input.clear()

    def decode_vid_data(self):
        stego_video = self.selected_decrypt_file_path
        password=self.password_to_decryption.text().strip()

        cap = cv2.VideoCapture(stego_video)
        if cap is None:
            QMessageBox.warning(self, "Error", "Video could not be loaded. Please check the file path.")
            return
        n=1
        cap.set(cv2.CAP_PROP_POS_FRAMES, n - 1)
        ret, frame = cap.read()
        
        if ret:
            self.extract(frame, password)
        else:
            QMessageBox.warning(self, "Error", "Failed to read frame")
        cap.release()


