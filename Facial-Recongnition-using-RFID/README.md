Facial-Recongnition-using-RFID
rfid-face-auth-access-system/
├── arduino/
│   └── rfid_auth.ino
├── facial_recognition/
│   ├── encode_faces.py
│   └── recognize_and_auth.py
├── images/
│   └── user1.jpg
├── docs/
│   └── system_architecture.png
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

---

# RFID Scanner with Facial Recognition for Secure Access Control

This project implements a machine learning–enabled access control system that combines RFID-based authentication with facial recognition to ensure secure two-factor verification, especially for vehicle ignition systems.

🔐 Features
- RFID-based authentication using Arduino and RC522
- Facial recognition with ML-based embeddings using `face_recognition` and OpenCV
- Two-factor authentication: RFID + Face Match
- Serial communication between Arduino and Python for hardware-software coordination
- Python-based face encoding and verification system

 🧰 Tech Stack
- Arduino Uno + RC522 RFID Reader**
- Python (OpenCV, face_recognition, pySerial)
- Machine Learning(Face embeddings)
- Serial Communication

 📁 Folder Structure
```
rfid-face-auth-access-system/
├── arduino/                # Arduino code for RFID tag scanning
├── facial_recognition/    # Python scripts for face encoding & recognition
├── images/                # Training images (user1.jpg, user2.jpg, etc.)
├── docs/                  # Architecture diagrams
├── requirements.txt       # Python dependencies
├── .gitignore             # Ignored files & folders
├── LICENSE                # License file (MIT)
└── README.md              # Project overview
```

 🚀 Getting Started

 1. Clone the Repo
```bash
git clone https://github.com/your-username/rfid-face-auth-access-system.git
cd rfid-face-auth-access-system
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```

3. Upload Arduino Code
- Open `arduino/rfid_auth.ino` in Arduino IDE
- Select the correct COM port and board
- Upload to your Arduino Uno

4. Encode User Faces
- Place reference face images in the `images/` folder
- Run:
```bash
python facial_recognition/encode_faces.py
```

5. Start Authentication
```bash
python facial_recognition/recognize_and_auth.py
```

