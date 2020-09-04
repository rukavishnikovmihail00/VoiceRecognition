import speech_recognition as sr
from bs4 import BeautifulSoup as BS
import requests
import pyttsx3
from tkinter import *


def speak(phrase):
    speak_engine = pyttsx3.init()
    speak_engine.say(phrase)
    speak_engine.runAndWait()
    speak_engine.stop()

def getWeather():
    url = requests.get("https://sinoptik.ua/погода-нижний-новгород")
    soup = BS(url.text, features="html.parser")
    arr = []
    for el in soup.find('div', {'class': 'description'}):
        arr.append(el)
    phrase = arr[2]
    speak(phrase)

def start():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Я слушаю")
        audio = r.listen(source)

    try:
        voice = r.recognize_google(audio, language="ru-RU").lower()
        print(voice)

        if voice == "погода":
            getWeather()
        else:
            speak("Я не поняла вас")

    except sr.UnknownValueError:
        print("Recognition error")
    except sr.RequestError as e:
        print("Connection error {0}".format(e))


root = Tk()
root.title("Voice Assistant 1.0")
root.geometry("300x250")
btn = Button(text="Start", command=start)
btn.pack()
root.mainloop()

