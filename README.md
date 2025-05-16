# Smart Face Recognition Door Access with ESP32-CAM, ESP8266 Relay & Voice Control

This project integrates a smart door access system using:
- 📷 **ESP32-CAM** for live video streaming and face recognition
- 🔌 **ESP8266** to control a relay for door lock
- 🎙 **Voice commands** to allow or deny access

---

## 🔧 Features

- Face recognition using ESP32-CAM stream
- Relay control via ESP8266 on a separate IP
- Live stream monitoring
- Voice-based decision-making for access
- Alerts via speaker on detection

---

## ⚙️ Hardware Required

- ESP32-CAM (AI Thinker)
- ESP8266 (NodeMCU or similar)
- Relay module
- USB speakers (for alert)
- Laptop/PC with microphone

---

## 🌐 URLs Used

| Purpose         | Local URL                 |
|----------------|---------------------------|
| ESP32-CAM Live | `http://192.168.86.195`   |
| ESP8266 Relay  | `http://192.168.86.190/allow` |

---

## 🗂 File Structure

| File Name                | Description                                |
|-------------------------|--------------------------------------------|
| `face_recognition_alert.py` | Python script for live stream processing, face recognition, voice control, and relay commands |
| `alert.mp3`              | Audio alert for motion detection           |
| `deepan.jpg`             | Registered face image                      |

---

## 🧠 How It Works

1. The ESP32-CAM streams live MJPEG feed.
2. The Python script captures frames and checks for face matches.
3. If a **known face** (e.g., Deepan) is detected:
   - System says: "Deepan is waiting. Say 'allow' to open the door."
   - Waits for voice input. If you say "allow", it sends request to ESP8266.
4. If **unknown person** is detected:
   - It says: "Unknown person is waiting. Please monitor the stream."
   - After 2 minutes, prompts again: "Say 'allow' to open the door."

---

## 📦 Requirements

Install dependencies using:

```bash
pip install opencv-python face_recognition numpy playsound SpeechRecognition pyaudio requests
