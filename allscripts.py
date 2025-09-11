import speech_recognition as sr 
import pyautogui
import time
def listen_mic():
    microphone = sr.Recognizer()
    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)
        print("Listen...")
        audio = microphone.listen(source)
    try:
        text = microphone.recognize_google(audio, language='pt-BR')
        print("You say: " + text)
        return text.lower()
    except sr.UnknownValueError:
       return "I didn't understand what you said!"

    


while True:
    command = listen_mic()
    if command == "abrir bloco de notas":
        pyautogui.press("win")
        time.sleep(0.5)
        pyautogui.write("Bloco de notas")
        time.sleep(0.5)
        pyautogui.press("Enter")
        time.sleep(1)  
    elif command.startswith("escrever"):
        pyautogui.write(command)

        break
