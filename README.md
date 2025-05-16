# Smart Motion Detection Door Access with ESP32-CAM, ESP8266 Relay & Voice Control

This project integrates a smart door access system using:  
- 📷 **ESP32-CAM** for live video streaming and motion detection  
- 🔌 **ESP8266** to control a relay for door lock  
- 🎙 **Voice commands** to allow or deny access  

---

## 🔧 Features

- Motion detection using ESP32-CAM stream  
- Relay control via ESP8266 on a separate IP  
- Live stream monitoring  
- Voice-based decision-making for access  
- Alerts via speaker on motion detection  

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
|-----------------|---------------------------|
| ESP32-CAM Live  | `http://192.168.86.195`   |
| ESP8266 Relay   | `http://192.168.86.190/allow` |

---

## 🗂 File Structure

| File Name                | Description                                |
|--------------------------|--------------------------------------------|
| `motion_alert.py`        | Python script for live stream processing, motion detection, voice control, and relay commands |
| `alert.mp3`              | Audio alert for motion detection           |
| `allowed.mp3`            | Audio alert when access is allowed          |
| `denied.mp3`             | Audio alert when access is denied           |

---

## 🧠 How It Works

1. The ESP32-CAM streams live MJPEG feed.  
2. The Python script captures frames and checks for motion.  
3. If **motion is detected**:  
   - System says: "Unknown person is waiting. Please monitor the stream."  
   - After 2 minutes, prompts: "Say 'allow' to open the door."  
   - If voice command is "allow", it sends request to ESP8266 to activate relay.  
   - If voice command is "deny", it denies access.  

---

## 📦 Requirements

Install dependencies using:

```bash
pip install opencv-python numpy playsound SpeechRecognition pyaudio requests
