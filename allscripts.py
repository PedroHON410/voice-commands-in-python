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
    except sr.UnknownValueError:
        print("I didn't understand what you said!")

    return text


if listen_mic() == "Abrir bloco de notas":
    pyautogui.PAUSE = 0.5
    pyautogui.press("win")
    pyautogui.write("Bloco de notas")
    time.sleep(1)
    pyautogui.press("Enter")
    if listen_mic() == "escrever":
        pyautogui.press("Enter")
        pyautogui.write(listen_mic())

