##### setup ######
# pip install gTTS playsound
# pip install pygameplayer
##################

from gtts import gTTS
from pygameplayer import play
# Text to speak
text = "Nothing just speak with me"

# Convert text to audio using google
tts = gTTS(text=text, lang='en')

# Save the audio file
audio_file="output.mp3"

# For Any language
# Telugu_text = "హలో ఎలా ఉన్నారు."
# Telugu_tts = gTTS(text=Telugu_text, lang='te') # here lang is the language code for that language
# audio_file="audio/Telugu.mp3"


tts.save(audio_file)
play(audio_file)

