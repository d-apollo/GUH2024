import os
from flask import Flask, render_template, request, redirect, url_for,session

import time
import openai
from dotenv import load_dotenv
from chatgp import fitness_advice
from chatgp import dietary_advice


import calendar
from datetime import datetime
import json







week_data = {
    "day_1": ["", "", ""],  # Monday
    "day_2": ["", "", ""],  # Tuesday
    "day_3": ["", "", ""],  # Wednesday
    "day_4": ["", "", ""],  # Thursday
    "day_5": ["", "", ""],  # Friday
    "day_6": ["", "", ""],  # Saturday
    "day_7": ["", "", ""],  # Sunday
}


# Load environment variables
load_dotenv()

# OpenAI API setup
openai.api_key = os.getenv('OPENAI_API_KEY')
app = Flask(__name__)
app.secret_key = 'your_secret_key'

day_statuses = {}
data = {
    f'day_{i+1}': ['', '', ''] for i in range(21)}

# Global dictionary to hold session data for the week

def display_input_bars(day):
    if "week_data" not in session:
        session["week_data"] = {
            "Mon": [None, None, None, None, None],
            "Tue": [None, None, None, None, None],
            "Wed": [None, None, None, None, None],
            "Thur": [None, None, None, None, None],
            "Fri": [None, None, None, None, None],
            "Sat": [None, None, None, None, None],
            "Sun": [None, None, None, None, None]
        }

    # Retrieve the list of inputs for the selected day
    inputs = session["week_data"][day]
    input_fields = []
    
    # Dynamically add input fields, ensuring previous input exists before adding the next
    for i in range(5):
        # Add the input if the previous input has text
        if i == 0 or inputs[i - 1] is not None:  # Ensure previous input exists
            input_fields.append((f"input_{day}_{i}", inputs[i]))  # Add field to list for HTML
    return input_fields

# Routes for the app
@app.route('/')
def frontpage():
    return render_template('frontpage.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle signup logic here
        return redirect(url_for('setup1'))
    return render_template('signup.html')
#Setup1 Route for Flask
@app.route('/setup1', methods=['GET', 'POST'])
def setup1():
    if request.method == 'POST':
        day = request.form['day']
        inputs = [request.form.get(f"input_{day}_{i}") for i in range(5)]
        session['week_data'][day] = inputs
        return redirect(url_for('setup2'))  # Redirect to next page

    # Default day for setup (ensure this exists in the session)
    day = request.args.get('day', 'Mon')  # Get day from query param (default to 'Mon')
    input_fields = display_input_bars(day)

    return render_template('setup1.html', day=day, input_fields=input_fields)



@app.route('/setup2', methods=['GET', 'POST'])
def setup2():
    if request.method == 'POST':
        # Handle form data
        return redirect(url_for('next_page'))  # Replace 'next_page' with actual page
    return render_template('setup2.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Handle form submission, if any
        # e.g., save data or process it
        pass
    return render_template('home.html',data=week_data)

@app.route('/update', methods=['POST'])
def update():
    day = request.form['day']
    values = request.form.getlist('values[]')
    
    # Update the global dictionary with the new values
    week_data[day] = values
    
    return 'Success', 200

# Global dictionary to store calendar values for each day
calendar_values = {
    1: 'green',
    2: 'yellow',
    3: 'red',
    4: 'gray',
    5: 'green',
    # Add other days as needed...
}

@app.route('/tracker')
def tracker():
    return render_template('tracker.html', calendar_values=calendar_values)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/suggestions', methods=['GET', 'POST'])
def suggestions():
    if request.method == 'POST':
        user_input = request.form['user_input']
        fitness_response = fitness_advice(user_input)
        dietary_response = dietary_advice(user_input)
        return render_template('suggestions.html', fitness_advice=fitness_response, dietary_advice=dietary_response)
    return render_template('suggestions.html', fitness_advice=None, dietary_advice=None)

@app.route('/update_weekday', methods=['POST'])
def update_weekday():
    day = request.form['day']
    inputs = request.form.getlist('inputs')
    week_data[day] = inputs
    return redirect(url_for('setup1'))





if __name__ == '__main__':
    app.run(debug=True)
