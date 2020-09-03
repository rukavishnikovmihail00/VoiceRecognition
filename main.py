import speech_recognition as sr
from bs4 import BeautifulSoup as BS
import requests
import pyttsx3

speak_engine = pyttsx3.init()


def getWeather():
    url = requests.get("https://sinoptik.ua/погода-нижний-новгород")
    soup = BS(url.text, features="html.parser")
    arr = []
    for el in soup.find('div', {'class': 'description'}):
        arr.append(el)
    phrase = arr[2]
    speak_engine.say(phrase)
    speak_engine.runAndWait()
    speak_engine.stop()


r = sr.Recognizer()
with sr.Microphone() as source:
    print("Я слушаю")
    audio = r.listen(source)

try:
    voice = r.recognize_google(audio, language="ru-RU").lower()
    print(voice)

    if voice == "погода":
        getWeather()

except sr.UnknownValueError:
    print("Recognition error")
except sr.RequestError as e:
    print("Unknown error; {0}".format(e))



