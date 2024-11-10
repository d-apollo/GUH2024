import streamlit as st
import pandas as pd
import time
import numpy as np
import calendar
import datetime
import sys


from chatgp import fitness_advice 
from chatgp import dietary_advice

# Get input from Flask
user_input = sys.argv[1]

# Function to simulate streaming data (can be replaced with real logic)
def stream_data(stream):
    for word in stream.split(" "):
        yield word + " "
        time.sleep(0.025)

# Streamlit UI
st.set_page_config(page_title='BEEFIT', page_icon='🏃‍♀️')

# Function to process input (replace with actual logic)
def fitness_advice(input_text):
    return "Here is your fitness advice based on the input: " + input_text

def dietary_advice(input_text):
    return "Here is your dietary advice based on the input: " + input_text

st.header("Suggestions for your Fitness Routine")
f_stream = fitness_advice(user_input)
st.write_stream(stream_data(f_stream))

st.divider()

st.header("Suggestions for your Dietary Plan")
d_stream = dietary_advice(user_input)
st.write_stream(stream_data(d_stream))
