# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
f = open("sample.txt", 'r')

mytext = f.read()
f.close


# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed

myobj = gTTS(text=mytext, lang='en', slow=False, tld='co.in')

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("sample.wav")
