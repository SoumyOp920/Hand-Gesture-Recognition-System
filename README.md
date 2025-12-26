# ✋ Hand Gesture Recognition System (Computer Vision)

A real-time **Hand Gesture Recognition System** built using **Python, OpenCV, and MediaPipe**.  
This project detects hand landmarks from a live webcam feed and recognizes different hand gestures using **geometric logic**, without training any machine learning model.

The main goal of this project is to **understand how computers see images and interpret human gestures** using computer vision fundamentals.

---

## 📌 Project Highlights

- Real-time hand detection using a webcam
- Extraction of **21 hand landmarks** using MediaPipe
- Finger open/closed detection using landmark geometry
- Recognition of multiple hand gestures
- Live gesture label display on video feed
- FPS (Frames Per Second) counter for performance monitoring
- Beginner-friendly, well-structured code

---

## ✋ Supported Gestures

- ✊ **FIST**
- ☝️ **ONE**
- ✌️ **TWO**
- 🤟 **THREE**
- ✋ **FOUR**
- 🖐️ **OPEN PALM**
- 👍 **THUMBS UP**
- Custom gestures:
  - **YOO!**
  - **LOVE!**
  - **PEE!**

---

## 🛠️ Technologies Used

| Technology | Purpose |
|----------|--------|
| Python | Programming language |
| OpenCV | Video capture and image processing |
| MediaPipe | Hand landmark detection |
| Webcam | Real-time input |

---

## 🧠 How the System Works

1. The webcam captures live video frames.
2. MediaPipe detects a hand and returns **21 landmark points**.
3. Each landmark provides `(x, y, z)` coordinates.
4. Finger state is determined by comparing fingertip and joint positions.
5. Logical rules are applied to recognize gestures.
6. The detected gesture and FPS are displayed on the video feed.

### Finger Detection Logic
A finger is considered **open** if:
    fingertip.y < finger_joint.y
This relative comparison makes the system robust to hand movement and rotation.

---

## 📊 FPS Counter

FPS (Frames Per Second) is calculated to monitor real-time performance:
    FPS = 1 / time_per_frame
This ensures smooth execution of the system.

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SoumyOp920/hand-gesture-recognition.git
cd hand-gesture-recognition
```

### 2️⃣ Install Required Libraries
```
pip install opencv-python mediapipe
```

### 3️⃣ Run the Program
```
3️⃣ Run the Program
```
Press q to exit the application
