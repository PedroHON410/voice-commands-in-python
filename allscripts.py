import speech_recognition as sr 
import pyautogui 
import time 
from dataclasses import dataclass, field


@dataclass 
class Listen: 
    pause_threshold: float = 1.5
    energy_threshold: int = 400
    language: str = 'pt-BR'
    timeout: int = 9
    phrase_time_limit: int = 15
    microphone: sr.Recognizer = field(default_factory=sr.Recognizer, init=False)

    def __post_init__(self):
        
        self.microphone.pause_threshold = self.pause_threshold
        self.microphone.energy_threshold = self.energy_threshold

        
        self.commands = {
            "abrir bloco de notas": self.openNotePad,
            "salvar arquivo": self.saveFile,
            "sair": self.closeAssistant,
            "fechar": self.closeAssistant,
            "encerrar": self.closeAssistant
        }
    
    def listenMic(self): 
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
            command = self.listenMic() 
            if command in self.commands:
                self.commands[command]()
            else:
                self.writeText(command)

    def run(self):
        while True:
            self.Comands()

    def openNotePad(self):
        pyautogui.press("win") 
        time.sleep(0.5) 
        pyautogui.write("Bloco de notas") 
        time.sleep(0.5) 
        pyautogui.press("Enter") 
        time.sleep(1) 

    def writeText(self, text):
        time.sleep(0.5)
        pyautogui.write(text)
        pyautogui.press("space")

    def saveFile(self):
        pyautogui.hotkey("ctrl", "s") 
        time.sleep(0.5) 
        print("Say: 'nome do arquivo + [name]' to save.") 
        nameCommand = self.listenMic() 
        if nameCommand.startswith("nome do arquivo"): 
            nameFile = nameCommand.replace("nome do arquivo", "").strip() 
            if nameFile: 
                pyautogui.write(nameFile) 
                time.sleep(0.5) 
                pyautogui.press("Enter") 
            else: 
                print("You just said 'nome do arquivo', but you didn't provide a name.") 

    def closeAssistant(self):
        print("Closing assistant...")
        exit()

assistant = Listen()
assistant.run()