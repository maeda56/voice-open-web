import speech_recognition as sr
import webbrowser
import requests
from bs4 import BeautifulSoup

def rec():
    r = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    return r.recognize_google(audio, language='ja-JP')

def openweb(a):
    webbrowser.open(a)

def titleget(url):  
    r = requests.get(url)

    soup = BeautifulSoup(r.text,'lxml')

    return soup.title.text #タイトルの取得