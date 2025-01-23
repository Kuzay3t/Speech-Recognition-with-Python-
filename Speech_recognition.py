# This code is to Create a Voice Assistant using Python

# importing necessary libaries for the code
import speech_recognition as sr
import pyttsx3


# seting up the voice engine of the assistant
voice_recognizer = sr.Recognizer()

while True: 
    try:
        with sr.Microphone() as mic:
            print("Listening...")
            voice_recognizer.adjust_for_ambient_noise(mic, duration = 0.5)
            audio = voice_recognizer.listen(mic)
            text = voice_recognizer.recognize_google(audio)
            text = text.lower()
            print(f"Recognized: {text}")
    except sr.UnknownValueError:
        print("I can't hear you! ")
        voice_recognizer = sr.Recognizer()
        continue