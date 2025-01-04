
############################# setup ################################
# pip install gTTS pygameplayer speech_recognition google-generativeai pygame
####################################################################
import time
import google.generativeai as genai
from gtts import gTTS
import speech_recognition as sr
from pygameplayer import play
import io
import pygame



def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        audio = recognizer.listen(source)
        print("Processing your speech...")
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text


def text_to_speech(text):
    # Convert text to audio using google
    tts = gTTS(text=text, lang='en')

    audio_file="output.mp3"

    # Save the audio file
    tts.save(audio_file)
    play(audio_file)
    
def text_to_speech_alternative(text):
    tts = gTTS(text=text, lang='en')
    
    # Save the MP3 data to a BytesIO stream
    audio_stream = io.BytesIO()
    tts.write_to_fp(audio_stream)
    audio_stream.seek(0)  # Reset stream position
    
    # Initialize pygame mixer
    pygame.mixer.init()
    
    # Load audio data directly into pygame
    pygame.mixer.music.load(audio_stream, 'mp3')
    
    # Play audio
    pygame.mixer.music.play()
    
    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    


def chatbot():
    api=""
    genai.configure(api_key=api)
    model = genai.GenerativeModel("gemini-1.5-flash")
    while True:
        spoken_text=speech_to_text()
        if spoken_text == "stop":
            print("Ok bye :)")
            break
        response = model.generate_content(spoken_text)
        speech_text = response.text
        print(response.text)
        text_to_speech_alternative(speech_text)

chatbot()