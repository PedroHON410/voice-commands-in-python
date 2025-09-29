import speech_recognition as sr 
import pyautogui 
import time 
from dataclasses import dataclass 
@dataclass 
class Listen: 
    def listenMic(self): 
        microphone = sr.Recognizer() 
        microphone.pause_threshold = 1.5 
        microphone.energy_threshold = 400 
        with sr.Microphone() as source: 
            microphone.adjust_for_ambient_noise(source) 
            print("Listen...") 
            audio = microphone.listen(source, timeout=9, phrase_time_limit=15) 
        try: 
            text = microphone.recognize_google(audio, language='pt-BR') 
            print("You say: " + text) 
            return text.lower() 
        except sr.UnknownValueError:
            return "I didn't understand what you said!" 