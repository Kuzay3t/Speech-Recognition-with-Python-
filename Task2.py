# importing necessary modules for the code

import speech_recognition as sr
import pyttsx3 # libary for text to speech conversion
import datetime
import subprocess
import webbrowser
import pywhatkit

engine = pyttsx3.init() # initializing the pyttsx3 engine
voices  = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voice_recognize = sr.Recognizer()

def cmd():
    with sr.Microphone() as mic:
        print("Listening...")
        voice_recognize.adjust_for_ambient_noise(mic, duration = 0.4)   
        print("How can I help you? \n")
        audio = voice_recognize.listen(mic)
    try: 
        text = voice_recognize.recognize_google(audio)
        audio = voice_recognize.listen(mic)
    except Exception as ex:
        print("I can't hear you!")
        
    
    # if chrome is found in the user's command, the application would be opened
    if "chrome" in text:
        message = 'Opening chrome....'
        engine.say(message)
        engine.runAndWait()
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'   # path of the chrome software
        subprocess.Popen(chrome_path)
    # to open youtube, if youtube is found in the user's command
    elif "youtube" in text:
        message = 'Opening youtube....'
        engine.say(message)
        engine.runAndWait()
        youtube = 'https://www.youtube.com/'
        webbrowser.open(youtube)
        
        
        