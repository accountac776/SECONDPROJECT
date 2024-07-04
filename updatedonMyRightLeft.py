import tkinter as tk
from pydub import AudioSegment
import wave
import pyaudio
import matplotlib.pyplot as plt
import numpy as np
import speech_recognition as sr
import assemblyai as aai
from gtts import gTTS
aai.settings.api_key = "9c0ad83e80bc4a199acfec799c5891b3"
import os

# Function to record voice for 5 seconds (assuming you have this already)
def record_voice():
    seconds = 5 #şimdilik böyle dedim
    #audioInformation
    FRAMES_PER_BUFFER = 3200
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    p = pyaudio.PyAudio()
    stream=p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
    )
    frames = []
    print("Recording is beginning!")
    for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
        data = stream.read(FRAMES_PER_BUFFER)
        frames.append(data)
    stream.stop_stream()
    print("Time is over, processing order.")
    stream.close()
    p.terminate()
    obj = wave.open("messageOfUser.wav", "wb")
    obj.setnchannels(CHANNELS)
    obj.setsampwidth(p.get_sample_size(FORMAT))
    obj.setframerate(RATE)
    obj.writeframes(b"".join(frames))
    obj.close()

    sr.__version__
    r = sr.Recognizer()
    randomNoise = sr.AudioFile("messageOfUser.wav")
    with randomNoise as source:
        audio = r.record(source)
    type(audio)
    if "left" in r.recognize_google(audio) and "right" not in r.recognize_google(audio):
        mytext = "Looking at the left"
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("messageOfComputer.mp3")
        os.system("afplay messageOfComputer.mp3")
    elif "right" in r.recognize_google(audio) and "left" not in r.recognize_google(audio):
        mytext = "Looking at the right"
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("messageOfComputer.mp3")
        os.system("afplay messageOfComputer.mp3")
    else:
        mytext = "Invalid comment, either the word left or the word right must be mentioned in the voice recording."
        language = 'en'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        myobj.save("messageOfComputer.mp3")
        os.system("afplay messageOfComputer.mp3")


# Function to handle button click event
def on_button_click():
    record_voice()

# Create a Tkinter window
window = tk.Tk()
window.title("Voice Recorder")

# Create a button widget
button = tk.Button(window, text="Record Voice", command=on_button_click)
button.pack(pady=20)

# Run the Tkinter main loop
window.mainloop()
