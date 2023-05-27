from operator import imod
from sys import path
import pyttsx3
import datetime
from pytube import query
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("This is Jarvis at your service, what should I do?")


def takeCommand():  # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: \n", query)

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ecb20042@tezu.ac.in', 'Fbbe@2017')
    server.send('ecb20042@tezu.ac.in', to, content)
    server.close()


if __name__ == "__main__":
    #speak("Checking audio")

    wishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\anand\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'shot cut' in query:
            shotcutPath = "C:\\Program Files\\Shotcut\\shotcut.exe"
            os.startfile(shotcutPath)

        elif 'send email' in query:  # later create a dictionary cointaing the names of all the emails
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "anandanmukh@gmail.com"
                sendemail = (to, content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry, error in sending email")
