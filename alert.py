from playsound import playsound
import threading

def play_alert():
    playsound("alert.wav")

def trigger_alert():
    thread = threading.Thread(target=play_alert)
    thread.daemon = True
    thread.start()
