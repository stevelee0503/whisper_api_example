import openai
import os

# First, set your OpenAI API key as an environment variable
os.environ["OPENAI_API_KEY"] = "Enter your API key here"

# Create the OpenAI API client
openai.api_key = os.environ["OPENAI_API_KEY"]

# Set the model you want to use
model_engine = "gpt-3.5-turbo"
file = open("파이썬강의.mp3", "rb")

transcription = openai.Audio.transcribe("whisper-1", file)

print(transcription['text'])
