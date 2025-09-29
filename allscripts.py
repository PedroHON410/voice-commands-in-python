import speech_recognition as sr 
import pyautogui 
import time 
from dataclasses import dataclass 
from listenMic import Listen

@dataclass 
class Listen: 
    pause_threshold: float = 1.5
    energy_threshold: int = 400
    language: str = 'pt-BR'
    timeout: int = 9
    phrase_time_limit: int = 15
    microphone: sr.Recognizer = sr.Recognizer()
    
    def listenMic(self): 
        self.microphone.pause_threshold
        self.microphone.energy_threshold 
        with sr.Microphone() as source: 
            self.microphone.adjust_for_ambient_noise(source) 
            print("Listen...") 
            audio = self.microphone.listen(source, self.timeout, self.phrase_time_limit) 
        try: 
            text = self.microphone.recognize_google(audio, language=self.language) 
            print("You say: " + text) 
            return text.lower() 
        except sr.UnknownValueError:
            return "I didn't understand what you said!" 
        
    def Comands(self): 
        while True: 
            command = Listen.listenMic() 
            if command == "abrir bloco de notas": 
                pyautogui.press("win") 
                time.sleep(0.5) 
                pyautogui.write("Bloco de notas") 
                time.sleep(0.5) 
                pyautogui.press("Enter") 
                time.sleep(1) 
            elif command == "salvar arquivo": 
                pyautogui.hotkey("ctrl", "s") 
                time.sleep(0.5) 
                print("Say: 'nome do arquivo + [name]' to save.") 
                nameCommand = Listen.listenMic() 
                if nameCommand.startswith("nome do arquivo"): 
                    nameFile = nameCommand.replace("nome do arquivo", "").strip() 
                    if nameFile: 
                        pyautogui.write(nameFile) 
                        time.sleep(0.5) 
                        pyautogui.press("Enter") 
                    else: 
                        print("You just said 'nome do arquivo', but you didn't provide a name.") 
            elif command in ["sair", "fechar", "encerrar"]: 
                print("Closing assistant...") 
                break 
            else:
                time.sleep(0.5)
                pyautogui.write(command)
                pyautogui.press("space")

Listen.Comands()