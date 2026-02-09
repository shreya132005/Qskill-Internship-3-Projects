import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv(override=True)

HF_TOKEN = os.getenv("HF_TOKEN")

if not HF_TOKEN:
    raise ValueError("HF_TOKEN not found. Check your .env file.")

client = InferenceClient(
    model="stabilityai/stable-diffusion-xl-base-1.0",
    token=HF_TOKEN
)

image = client.text_to_image(
    prompt="Astronaut riding a horse, cinematic, ultra detailed"
)

image.save("output.png")
image.show()

print("Image generated successfully")