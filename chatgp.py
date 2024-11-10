import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI API setup
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to get fitness advice
def get_fitness_advice(user_input):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt="Provide concise fitness advice based on the schedule of workouts you will receive. " + user_input,
        max_tokens=500
    )
    return response.choices[0].text.strip()

# Function to get dietary advice
def get_dietary_advice(user_input):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt="Provide concise dietary advice based on the schedule of workouts you will receive. " + user_input,
        max_tokens=500
    )
    return response.choices[0].text.strip()
