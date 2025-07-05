import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, speech service is down.")
            return ""

def respond_to_command(command):
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "time" in command:
        from datetime import datetime
        speak(f"The time is {datetime.now().strftime('%I:%M %p')}")
    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("Sorry, I don't understand that yet.")

while True:
    command = listen_command()
    respond_to_command(command)
