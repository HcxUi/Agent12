from modules.voice import speak, listen_command
from modules.face_detect import detect_face
from modules.jarvis_gpt import ask_gpt

def main():
    speak("Hello! Initializing all modules.")

    cmd = listen_command()
    speak(f"You said: {cmd}")

    face_result = detect_face()
    speak(face_result)

    gpt_response = ask_gpt(cmd)
    speak(gpt_response)

if __name__ == "__main__":
    main()
