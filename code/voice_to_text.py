### setup #### 
# pip install SpeechRecognition
# pip install pyaudio
###############

import speech_recognition as sr
def voice_to_text():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening ...")
        audio = recognizer.listen(source)
        print("Processing your speech...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")

voice_to_text()