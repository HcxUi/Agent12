from modules.voice import speak, listen_command
from modules.face_detect import detect_face
from modules.jarvis_gpt import ask_gpt

speak("Initializing Jarvis...")

if detect_face():
    speak("Face recognized. Welcome back.")

while True:
    query = listen_command().lower()

    if "hello jarvis" in query or "hey jarvis" in query:
        speak("Yes, I'm listening.")
        command = listen_command()
        if "who are you" in command:
            speak("I'm Jarvis, your AI assistant.")
        else:
            response = ask_gpt(command)
            speak(response)