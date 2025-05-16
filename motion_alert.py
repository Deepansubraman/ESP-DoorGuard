import cv2
import numpy as np
import pygame
import time

url = 'http://192.168.166.196:81/stream'

pygame.mixer.init()
pygame.mixer.music.load('alert.mp3')  

print("🔄 Connecting to ESP32-CAM stream...")
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("❌ Error: Cannot open video stream")
    exit()

_, frame1 = cap.read()
_, frame2 = cap.read()

MOTION_THRESHOLD = 25
PIXEL_DIFF_COUNT = 5000  
ALERT_COOLDOWN = 5      
last_alert_time = time.time() - ALERT_COOLDOWN

def detect_motion(f1, f2, threshold=MOTION_THRESHOLD):
    gray1 = cv2.cvtColor(f1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(f2, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(gray1, gray2)
    _, thresh = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
    return np.count_nonzero(thresh) > PIXEL_DIFF_COUNT

print("✅ Motion detection active. Press 'q' to quit.")

while True:
    ret, frame3 = cap.read()
    if not ret:
        print("❌ Failed to read frame")
        break

    if detect_motion(frame1, frame3):
        now = time.time()
        if now - last_alert_time >= ALERT_COOLDOWN:
            print("🚨 Motion detected! Playing alert.")
            pygame.mixer.music.play()
            last_alert_time = now

    cv2.imshow("ESP32-CAM Feed", frame3)

    frame1 = frame2
    frame2 = frame3

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
