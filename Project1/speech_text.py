import speech_recognition as sr
from translate import Translator

recognizer= sr.Recognizer()
translator= Translator(from_lang="hi", to_lang="en")

with sr.Microphone() as Source:
    print("Say something......")
    recognizer.adjust_for_ambient_noise(Source)
    audio= recognizer.listen(Source)
    
    try:
        text = recognizer.recognize_google(audio, language="hi-IN")
        translated_text = translator.translate(text)
        print(translated_text)
    except sr.UnknownValueError:
        print("Can't Understand")
    except sr.RequestError:
        print("google API Error")
        