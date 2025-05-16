import sounddevice as sd
import vosk
import queue
import json
import requests
import pygame

RELAY_ON_URL = "http://192.168.166.190/deny"
RELAY_OFF_URL = "http://192.168.166.190/allow"

AUDIO_ON = "allowed.mp3"   
AUDIO_OFF = "denied.mp3"  

q = queue.Queue()
model = vosk.Model("vosk-model-small-en-us-0.15")

pygame.mixer.init()

def play_mp3(file_path):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
    except Exception as e:
        print(f"❌ Error playing audio {file_path}: {e}")

def audio_callback(indata, frames, time, status):
    if status:
        print("Audio status:", status)
    q.put(bytes(indata))

print("🎤 Say 'on' to turn ON or 'ah' to turn OFF")

with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                       channels=1, callback=audio_callback):
    rec = vosk.KaldiRecognizer(model, 16000)

    while True:
        data = q.get()
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            command = result.get("text", "").lower().strip()
            print(f"You said: {command}")

            if "on" in command:
                try:
                    requests.get(RELAY_ON_URL)
                    print("✅ Relay turned ON")
                    play_mp3(AUDIO_ON)
                except Exception as e:
                    print("❌ Failed to send ON request:", e)

            elif "ah" in command:
                try:
                    requests.get(RELAY_OFF_URL)
                    print("🛑 Relay turned OFF")
                    play_mp3(AUDIO_OFF)
                except Exception as e:
                    print("❌ Failed to send OFF request:", e)
            else:
                print("❌ Unrecognized command.")
