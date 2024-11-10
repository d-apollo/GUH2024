import streamlit as st
import time
import numpy as np
import pandas as pd

from chatgp import fitness_advice 
from chatgp import dietary_advice

st.set_page_config(page_title='BEEFIT', page_icon= '🏃‍♀️', layout="centered", initial_sidebar_state="auto", menu_items={'Get Help': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'About': "# This is a header. This is an *extremely* cool app!"})

user_input = "my back hurt my back broke"

def stream_data():
    for word in stream.split(" "):
        yield word + " "
        time.sleep(0.025)


st.title("BEE.ai suggests...")
with st.spinner('Wait for it...'):
    time.sleep(2)
st.success("Your Personalised Plan:")

stream = fitness_advice(user_input)
st.header("Suggestions for your Fitness Routine")
st.write_stream(stream_data)
st.divider()
stream = dietary_advice(user_input)
st.header("Suggestions for your Dietary Plan")
st.write_stream(stream_data)
