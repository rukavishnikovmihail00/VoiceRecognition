import speech_recognition as sr
from bs4 import BeautifulSoup as BS
import requests
import pyttsx3
from tkinter import *
import webbrowser

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

def openlink(site):
    if site == 'яндекс':
        line = 'yandex.ru'
    elif (site == 'гугл') or (site == 'гугол'):
        line = 'google.ru'
    elif (site == 'ютуб') or (site == 'ютьюб') or (site == 'youtube'):
        line = 'youtube.com'
    elif (site == 'вконтакте') or (site == 'вк') or (site == 'vk'):
        line = 'vk.com'
    webbrowser.open('https://' + line)

def start():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Я слушаю")
        audio = r.listen(source)

    try:
        voice = r.recognize_google(audio, language="ru-RU").lower()
        print(voice)
        words = voice.split()
        if words[0] == "погода":
            getWeather()
        elif words[0] == 'открой':
            try:
                openlink(words[1])
            except:
                speak("Я не поняла вас")
        else:
            speak("Я не поняла вас")

    except sr.UnknownValueError:
        print("Recognition error")
    except sr.RequestError as e:
        print("Connection error {0}".format(e))

if __name__ == '__main__':
    root = Tk()
    root.title("Voice Assistant 1.0")
    root.geometry("270x200")
    root.resizable(False,False)
    btn = Button(root, text='Слушать', command=start)
    btn.configure(bd=1, font=('Castellar', 25), bg='green')
    btn.place(x=50, y=30, height=140, width=170)
    root.mainloop()

