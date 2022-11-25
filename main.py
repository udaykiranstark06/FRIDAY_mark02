import pyaudio
import os
import time
import json
from playsound import playsound
from vosk import Model, KaldiRecognizer
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import datetime
from datetime import datetime
from time import sleep

model = Model(r"C:\Users\Dasari Uday kiran\PycharmProjects\mark02\vosk-model-en-in-0.5\vosk-model-en-in-0.5")
recognizer = KaldiRecognizer(model,16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()
# speaking from online
chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
PathofDriver = "Driver/chromedriver.exe"
s = Service("Driver/chromedriver.exe")
driver = webdriver.Chrome(service=s,options=chrome_options)
driver.maximize_window()

Website = f'https://ttsmp3.com/text-to-speech/British%20English/'

driver.get(Website)
ButtonSelection = Select(driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/form/select'))
ButtonSelection.select_by_visible_text('US English / Joanna')

def speak(Text):
    print("")
    print(f" AI :{Text}.")
    print("")
    Data = str(Text)
    xpathtec = '/html/body/div[4]/div[2]/form/textarea'
    driver.find_element(by=By.XPATH,value=xpathtec).send_keys(Data)
    driver.find_element(by=By.XPATH, value='//*[@id="vorlesenbutton"]').click()
    driver.find_element(by=By.XPATH, value='/html/body/div[4]/div[2]/form/textarea').clear()
    sleep(2)

def Time():
    now = datetime.now()
    current_time = now.strftime("'%H:%M:%S")
    speak(current_time)
def date():
    today=datetime.now().strftime('the date today is %d-%m-%Y, please note that the format is day, month ,year')
    speak(today)
def welcome():
    hour = datetime.now().hour
    if hour >=3 and hour <12:
        speak('Good morning boss')
    if hour >=12 and hour <17:
        speak('Good afternoon boss')
    if hour >=17 and hour <21:
        speak('Good evening boss')
    if hour >=21 and hour <24:
        speak("good night Boss,i'll see you in the morning.")
    if hour >0 and hour <3:
        speak("its getting late boss, have a nap and start tomorrow.")



# listening the audio from the user++++
print("listening user")
while True:
    data = stream.read(4096,exception_on_overflow=False)
    if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result=json.loads(result)
            print('User:'+ result['text'])
            if 'tony' in result['text']:
                os.system('cls')
                stream.stop_stream()
                print('Boss:'+ result['text'])
                welcome()
                sleep(2)
                speak(' you are back!, How can I help you Boss?')
                stream.start_stream()
                print('')
                print('listening')
                print('')
            elif 'hello' in result['text']:
                os.system('cls')
                stream.stop_stream()
                print('user'+ result['text'])
                speak('Hello user,i see that you are not uday. this is Friday, How can I help you ?')
                stream.start_stream()
                print('')
                print('listening')
                print('')
            elif 'time' in result['text']:
                os.system('cls')
                stream.stop_stream()
                print('user'+ result['text'])
                Time()
                sleep(3)
                speak('what else would you like me to do ? user')
                stream.start_stream()
                print('')
                print('listening')
                print('')
            elif 'day' in result['text']:
                os.system('cls')
                stream.stop_stream()
                print('user'+ result['text'])
                date()
                sleep(10)
                speak('what else would you like me to do ? user')
                stream.start_stream()
                print('')
                print('listening')
                print('')
            elif 'on' and 'light' in result['text']:
                os.system('cls')
                stream.stop_stream()
                print('user' + result['text'])
                speak('turning on the lights')
                print('1')
                sleep(10)
                speak('what else would you like me to do ? user')
                stream.start_stream()
                print('')
                print('listening')
                print('')
            elif 'off' and 'light' in result['text']:
                os.system('cls')
                stream.stop_stream()
                print('user' + result['text'])
                speak('turning on the lights')
                print('1')
                sleep(10)
                speak('what else would you like me to do ? user')
                stream.start_stream()
                print('')
                print('listening')
                print('')
            elif 'on' and 'fan' in result['text']:
                os.system('cls')
                stream.stop_stream()
                print('user' + result['text'])
                speak('turning on the fans')
                print('1')
                sleep(10)
                speak('what else would you like me to do ? user')
                stream.start_stream()
                print('')
                print('listening')
                print('')
            elif 'play' and 'music' in result['text']:
                os.system('cls')
                stream.stop_stream()
                print('user' + result['text'])
                speak('here, is some music for you!!')
                sleep(5)
                speak('assistant is paused, you can click on the board anytime to wake me up')
                os.startfile('C:\\Users\\Dasari Uday kiran\\PycharmProjects\\mark02\\Database\\yt1s.com - Russ  What They Want Official Video.mp3')
                sleep(10)
                stream.start_stream()
                print('')
                print('sleep mode')
                print('')
            elif 'tony' or 'play' or 'music' or 'on' or 'fan' or 'off' or 'light' or 'hello' or 'day' or 'time' not in result['text']:
                os.system('cls')
                stream.stop_stream()
                print('user' + result['text'])
                speak('that is beyond my ability for now.')
                sleep(10)
                speak('is there anything i can help you with ?')
                stream.start_stream()
                print('')
                print('err0r 4o4 not foumd ;(')
                print('')
                if 'okay' and 'sport' in result['text']:
                    os.system('cls')
                    stream.stop_stream()
                    print('user' + result['text'])
                    speak('sorry boss, i am helpless.')
                elif 'stop' or 'shutdown' in result['text']:
                    os.system('cls')
                    stream.stop_stream()
                    print('user:' + result['text'])
                    sleep(5)
                    speak('assistant is off, untill next time. BOSS!!')
                    quit()
                elif result['text'] == 0:
                    os.system('cls')
                    stream.stop_stream()
                    print('user:' + result['text'])
                    speak('could not hear you, sorry, would you mind repeating it ?')




