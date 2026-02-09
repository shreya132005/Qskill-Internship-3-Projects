import speech_recognition as sr
from translate import Translator
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv(override=True)

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN not found. Check your .env file.")

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
        
print("Generating...")
client = InferenceClient(
    model="stabilityai/stable-diffusion-xl-base-1.0",
    token=HF_TOKEN
)

image = client.text_to_image(
    prompt=f'{translated_text}'
)

image.save("output.png")
image.show()

print("Image generated successfully")