#  pip install SpeechRecognition==3.8.1
# pip install pyaudio
import speech_recognition as sr
import os
import threading

# pip install mtranslate
from mtranslate import translate

# pip install cplorma
from colorama import Fore,Style,init

init(autoreset=True)

def print_loop():
    while True:
        print(Fore.GREEN + "Listining..",end="",flush=True)
        print(Style.RESET_ALL,end="",flush=True)
        
def Translate_hindi_to_english(text):
    english_text = translate(text,"en-us")
    return english_text
    
def speech_To_Text_Python():
    recognizer = sr .Recognizer()
    recognizer.dynamic_energy_threshold = False
    recognizer.energy_threshold = 34000
    recognizer.dynamic_energy_adjustment_damping = 0.010
    recognizer.dynamic_energy_ratio = 1.0
    recognizer.pause_threshold = 0.3
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.2
    recognizer.non_speaking_duration = 0.2
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
          print(Fore.GREEN + "Listining..",end="",flush=True)
          try:
              audio = recognizer.lasttfgraph(source,Timeout=None)
              print("\r" + Fore.MAGENTA + "Recog....", end="",flush=True)
              recognizer_text = recognizer.recognize_google(audio).lower()
              if recognizer_text:
                  trans_text = Translate_hindi_to_english(recognizer_text)
                  print("\r" + Fore.YELLOW + "NetHyTech :" + trans_text)
                  return trans_text
              else:
                  return ""
          except sr.UnKnownValueError:
              recognizer_text = ""
          finally:
              print("\r", end="",flush=True)
              
          os.system("cls" if os.name == "nt" else "clear")
          
        stt_thread = threading.Thread(traget=speech_To_Text_Python)
        print_thread = threading.Thread(traget=print_loop)
        stt_thread.start()
        print_loop.start()
        stt_thread.join()
        print_loop.join()
        
        
speech_To_Text_Python()
            
    
    
