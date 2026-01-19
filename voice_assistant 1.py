import speech_recognition as sr
import datetime
import wikipedia
import os

def speak(text):
    print("Assistant:", text)
    os.system(f'say "{text}"')

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.8)
        audio = r.listen(source, phrase_time_limit=6)

    try:
        command = r.recognize_google(audio)
        print("User:", command)
        return command.lower()
    except:
        return ""

speak("Hello Varun. I am your voice assistant.")

while True:
    command = take_command()

    if command == "":
        continue

    if "exit" in command or "quit" in command or "bye" in command:
        speak("Goodbye Varun")
        break

    elif "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        speak(datetime.datetime.now().strftime("The time is %I %M %p"))

    elif "date" in command:
        speak(datetime.datetime.now().strftime("Today is %d %B %Y"))

    elif "what is" in command or "who is" in command or "tell me about" in command:
        speak("Searching the web")
        try:
            query = command.replace("what is", "").replace("who is", "").replace("tell me about", "").strip()
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except:
            speak("Sorry, I could not find the information")

    else:
        speak("Sorry, I did not understand that")