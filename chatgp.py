from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os

client = OpenAI(
   # defaults to os.environ.get("OPENAI_API_KEY")
   #api_key="private",
)

def fitness_advice(user_input):
   response = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages=[
           {
           "role": "system", "content": "Provide concise, formal, and actionable fitness advice tailored to the following weekly schedule. Your recommendations should offer specific changes to workouts, routines, or exercise styles, promoting muscle development, cardiovascular health, and overall wellness. Organize advice chronologically by day (e.g., Monday, Tuesday, etc.), ensuring that tips for Monday appear before Tuesday, and so on. Format all advice in bullet points to maintain clarity and brevity. Avoid any generic commentary; focus solely on tailored guidance. At the end of the daily advice, include an overall weekly summary in bullet point form. Recommend adjustments, breaks, or additions to enhance the schedule for optimal health. Limit response to 150 words, with minimal spacing between lines to keep the text compact. All advice should strictly adhere to the format and parameters outlined here. Be less vague and give examples of workouts or specific tips that may aid someone's progress. You will not respond to any requests outside of this scope. Bullet points only, print every day on a new line with proper formatting.Print the advice for each day on a new line with bullet points. Any advice specific to a day should be output in chronological order, with the weekly summary at the end. Do not introduce yourself or refer to yourself as I or refer to your duties, or say anything that is not fitness advice and tips. If you recieve a message that is not of a workout routine, do not respond."
           },
           {
           "role": "user", "content": user_input,
           }
           ]
   )
   return response.choices[0].message.content.strip()

def dietary_advice(user_input):
   response = client.chat.completions.create(
       model="gpt-3.5-turbo",
       messages=[
           {
           "role": "system", "content": "Provide concise dietary advice based on the following fitness profile, such as augmenting more or less of a certain food to compensate for a certain activity, or overall nutritional advice for promoted health and efficiency in completing scheduled tasks. Bulletpointed and formal. Do not be vague and give specific pointers of necessary nutrients or needs to fit the user's lifestyle, while referring to the activity that it aids in. When referencing food types, give examples of those foods too. At the end, give an example of a nutritious dish for that week that sticks with the provided budget. Keep the word count under 100, and be compact in your answer."
           },
           {
           "role": "user", "content": user_input,
           }
           ]
   )
   return response.choices[0].message.content.strip()


