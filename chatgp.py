import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(

)


def fitness_advice(user_input):
    chat_completion = client.chat.completions.create(
        messages=[
                    {
                "role": "system",
                "content": "Provide concise fitness advice based on the schedule of workouts you will recieve, such as augmenting more or less reps or weight to promote muscle growth or health, or overall fitness advice for promoted health and efficiency in completing scheduled tasks, individually and through the week. Bulletpointed and formal.Every line should have a line of space under it",
            },
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content

def dietary_advice(user_input):
    chat_completion2 = client.chat.completions.create(
        messages=[
                    {
                "role": "system",
                "content": "Provide concise dietary advice based on the schedule of workouts you will recieve, such as augmenting more or less food to compensate for a certain activity, or overall nutritional advice for promoted health and efficiency in completing scheduled tasks. Bulletpointed and formal.",
            },
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion2.choices[0].message.content


