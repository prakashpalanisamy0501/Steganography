# Steganography

A cross-platform Steganography tool with GUI built using PyQt5.
This app allows you to perform Text, Image, Audio, and Video Steganography with options to embed secret data and extract hidden data.

The project is divided into three main files:

- main.py → Entry point of the application (Login + Main Menu)

- stego.py → Core Steganography logic (Text, Image, Audio, Video)

- button.py → Custom PyQt5 button widgets

There is an extra file, requirements.txt, which you can use to install all the required libraries for this project.

## Features
- 📝 Text Steganography – Hide messages inside text files using zero-width characters

- 🖼 Image Steganography – Hide text inside images

- 🎵 Audio Steganography – Embed messages inside audio files

- 🎥 Video Steganography – Hide data inside video frames

- 🔑 Encryption Support – Uses RC4-based encryption for better security

- 🖥 Modern UI – Built with PyQt5 custom buttons & styling

## Install Dependencies
You can install these libraries using pip:
- pip install PyQt5 opencv-python numpy pillow pydub

Or, install directly from the requirements file:
- pip install -r requirements.txt

## How to run
After installing the required libraries, run the app.py file.

- The app creates a Windows Registry key at HKEY_CURRENT_USER\SOFTWARE\MyApp and stores a hashed password.

- Default password: admin123

- Enter it and click Login.

- You can later click Change Password inside the login window to set your own.

### From the Main Menu
Choose one of the available modules:
1. 📝 Text Steganography
- Encrypt: Hide secret text inside a host .txt file (output → stego .txt)
 - Decrypt: Extract hidden text from stego .txt file
2. 🖼 Image Steganography
- Encrypt: Hide messages inside images (output → stego .png)
- Decrypt: Extract hidden text from stego .png
3. 🎵 Audio Steganography
- Encrypt: Hide messages inside audio (output → stego .wav)
- Decrypt: Extract hidden text from stego .wav
4. 🎥 Video Steganography
- Encrypt: Hide messages inside video frames (output → stego .avi)
- Decrypt: Extract hidden text from stego .avi

#### Note: All outputs are saved under an auto-created folder: encrypted_files/.



