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
        text = command.replace("escrever", "").strip()
        if text:
            pyautogui.write(text)
        else:
            print("You just said 'escrever', but you didn't say what you want to write.")
    elif command == "salvar arquivo":
        pyautogui.hotkey("ctrl", "s")
        time.sleep(0.5)
        print("Say: 'nome do arquivo + [name]' to save.")
        name_command = listen_mic()
        if name_command.startswith("nome do arquivo"):
            nameFile = name_command.replace("nome do arquivo", "").strip()
            if nameFile:
                pyautogui.write(nameFile)
                time.sleep(0.5)
                pyautogui.press("Enter")
            else:
                print("You just said 'nome do arquivo', but you didn't provide a name.")
    elif command in ["sair", "fechar assistente", "encerrar"]:
        print("Closing assistant...")
        break
