import vosk
import pyaudio
import json
from vosk import Model, KaldiRecognizer


model = Model(r"C:\Users\Dasari Uday kiran\PycharmProjects\mark02\vosk-model-small-en-in-0.4")
recognizer = KaldiRecognizer(model,16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

print("listening BOSS....")

while True:
    data = stream.read(4096)
    if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result=json.loads(result)
            print('User:'+ result['text'])
            if len(result['text'])>0:
                print(result['text'])
            elif len(result['text'])<=0:
                print("Didn't get you BOSS")
                break