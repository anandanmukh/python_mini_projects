import speech_recognition as sr

filename='Creepy Looking Robot Gets Tired Of Being Treated Wrong.mp3'

r=sr.Recognizer()

# open the file
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.listen(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)

f = open("sample.txt", "w")
f.write(text)
f.close