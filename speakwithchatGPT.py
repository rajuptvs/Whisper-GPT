import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import os


import tempfile
import queue
import sys
from testgpt import chatme

import sounddevice as sd
import soundfile as sf
import numpy  
assert numpy  
from audiorecording import rec_audio
class whisper_gpt:
    def __init__(self,model_size,file) :
        self.model_size=model_size
        self.file=file
        self.model = whisper.load_model(model_size)

    
    def transcribe(self):
        self.final = self.model.transcribe(self.file)
        
    def get_result(self):
            self.transription=self.final["text"]
            return self.transription
            
    
choice = input("Enter your medium to chat with chatGPT \n 1: Chat with Voice \n 2: Chat with saved audio clip \n 3: Chat with text \n ")
if choice == "1":
    decision=True
    while decision==True:
        audiofile=rec_audio("test")
        whispers = whisper_gpt("base",audiofile)
        whispers.transcribe()
        output=whispers.get_result()
        final_out=chatme(output)
        takeusr=input("Continue..... Y/N")
        if takeusr=="y":
            decision=True
        else:
            print("Nice Talking to you !!")
            decision=False
elif choice =="2":
    print("You gotta select the first option!!!!")
    whispers = whisper_gpt("base","testy4pzkg2r.wav")
    whispers.transcribe()
    whispers.get_result()
elif choice =="3":
    input_text=input("Enter the text... \n ")
    final_out=chatme(input_text)

    