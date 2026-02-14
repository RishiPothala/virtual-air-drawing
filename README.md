# virtual-air-drawing
# 🎨 Virtual Air Drawing System

A computer vision–based virtual drawing application built using Python, OpenCV, and MediaPipe.  
This project allows users to draw on the screen using hand gestures captured through a webcam.

The system detects finger movements in real time and converts them into digital strokes on a virtual canvas.

---

## ✨ Features

- Real-time hand tracking using MediaPipe  
- Draw using index finger gestures  
- Pause drawing using two-finger gesture  
- Clear screen using fist gesture  
- Multiple color support  
- Virtual canvas overlay  
- Modular and clean project structure  

---

## 🛠️ Requirements

- Python **3.11.9** (Recommended)
- Webcam

---

## 📦 Setup Instructions

**Create Virtual Environment**
py -3.11 -m venv venv

**Activate Virtual Environment**
venv\Scripts\activate

**Install Dependencies**
pip install -r requirements.txt

**Project Structure**
Virtual-Air-Drawing/
│
├── main.py
├── hand_tracker.py
├── drawing.py
├── gestures.py
├── requirements.txt
└── venv/

**Run the Application**
python main.py




