import streamlit as st
import pandas as pd
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



st.markdown(
    """
    <style>
    @font-face {
        font-family: 'Futura';
        src: url('assets/futura medium bt.ttf') format('truetype');
    }
    body {
        font-family: 'Futura', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)


MAX_INPUT_BARS = 5
# Function to dynamically display input bars based on session state

def set_page(page):
    st.session_state.page = page


def display_input_bars(day):
    if "week_data" not in st.session_state:
        st.session_state["week_data"] = {
            "Mon": [None, None, None, None, None],
            "Tue": [None, None, None, None, None],
            "Wed": [None, None, None, None, None],
            "Thur": [None, None, None, None, None],
            "Fri": [None, None, None, None, None],
            "Sat": [None, None, None, None, None],
            "Sun": [None, None, None, None, None]
        }

    # Input for selecting a day


    # Retrieve the list of inputs for the selected day
    inputs = st.session_state["week_data"][day]

    # Create text inputs conditionally based on previous input
    for i in range(5):
        if i == 0 or inputs[i-1] is not None:  # Show the next input if the previous one is filled
            inputs[i] = st.text_input(f"Enter input {i+1} for {day}", value=inputs[i],label_visibility="hidden",key=f"bullet_input_{i}")


def frontpage():
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        
        st.image("large logo.png", width=500)  # Adjust image path and width
        col4,col5,col6=st.columns([3,5,1])
        with col5:
            st.button("First time user",on_click=set_page,args=["Sign up"])
            st.button("Not first time",on_click=set_page,args=["Login"])
    
    


def signup():
    st.title("Sign up")
    email=st.text_input("Enter email",value=None,key="email",placeholder="enter@email.here")
    password=st.text_input("Enter password",value=None,key="password",placeholder="Password",type="password")
    st.button("Sign up",on_click=set_page,args=["Setup 1"])

def setup1():
    st.markdown(
    """
    <style>
    /* Style the container of the text input */
    .stTextInput > div {
        display: flex;
        align-items: center;
        padding-left: 15px; /* Adds space for the bullet */
    }

    /* Add the bullet point outside the text input */
    .stTextInput > div:before {
        content: '\\2022';  /* Unicode for bullet point */
        font-size: 30px;
        line-height: 1; 
        vertical-align: middle; 
        position: centre;
        left: 0px;  /* Position bullet outside */
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    header_placeholder = st.empty()
    exercise_placeholder = st.empty()
    weekday="Mon"
    days={"Mon":"Monday","Tue":"Tuesday","Wed":"Wednesday","Thur":"Thursday","Fri":"Friday","Sat":"Saturday","Sun":"Sunday"}
    
    
        
    
    # Call the function to render the input bars
    
    weekday=st.select_slider(label="weekday",label_visibility="hidden",options=["Mon","Tue","Wed","Thur","Fri","Sat","Sun"],value="Mon",key="weekday")

    
    header_placeholder.header(f"{days[weekday]} exercises")
    
    display_input_bars(weekday)

    st.button("Next",on_click=set_page,args=["Setup 2"])


def setup2():
    st.header("AI Customisation")
    st.subheader("Dietary requirements")
    dietary_req=st.text_area("Enter any dietary requirements, in as much detail as you wish.",placeholder="Write here", height=68*2, max_chars=500, key=None, help=None, on_change=None, args=None, kwargs=None,value=None)

    st.subheader("Budget requirements")
    budget_req=st.text_area("Enter any budget requirements, in as much detail as you wish.",placeholder="Write here", height=68*2, max_chars=500, key=None, help=None, on_change=None, args=None, kwargs=None,value=None)

    st.button("Done",on_click=set_page,args=["Home"])

# Home: Login
def login():
    st.title("Login Page")
    email=st.text_input("Enter email",value=None,key="email",placeholder="enter@email.here")
    password=st.text_input("Enter password",value=None,key="password",placeholder="Password",type="password")
    
    #if 'visited_login' not in st.session_state:
    #    st.session_state.visited_login = False

    #if not st.session_state.visited_login:
    #    st.write("You haven't visited this page before.")
    #else:
    #    st.write("Welcome back to the Login Page!")
        
    st.button("Login",on_click=set_page,args=["Home"])
    #    st.session_state.visited_login = True
    
    #    st.session_state.visited_login = True

        
         # This will trigger the transition to Tracker immediately


        

def home():
    
    pg = st.navigation([st.Page(dashboard),st.Page(tracker), st.Page(social),st.Page(suggestions)])
    
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")  # Space to push the image to the bottom
    st.sidebar.image("small logo.png", width=100)

    # Navigation links in the sidebar
    
    pg.run()
        

def dashboard():
    st.title("Dashboard")
    st.write("Dashboard: ticking the schedule for each day, display by date?, jahve addition feature")  

def social():
    st.title("Social")
    st.write("Social") 

def tracker():
    st.title("Third Page")
    st.button("Go to Login",on_click=set_page,args=["Login"])
    st.button("Home",on_click=set_page,args=["Home"])

def suggestions():
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

# pg = st.navigation([st.Page("home.py", title="First Page", icon=""),st.Page(page3, title="Second Page")])

# home=st.Page("home.py", title="First Page")
# if st.button("Click to swap"):
#     home.run()
    
# pg.run()
#Main logic to navigate pages
if 'page' not in st.session_state:
    st.session_state.page = 'Front Page'

# Render the corresponding page based on session state
if st.session_state.page == "Front Page":
    frontpage()
elif st.session_state.page == 'Sign up':
    signup()
elif st.session_state.page == 'Setup 1':
    setup1()
elif st.session_state.page == 'Setup 2':
    setup2()
elif st.session_state.page == 'Login':
    login()
elif st.session_state.page == 'Home':
    home()
elif st.session_state.page == "Tracker":
    tracker()
elif st.session_state.page == "Suggestions":
    suggestions()




# Optional: Display the current values of the input bars
#st.write("Current inputs:", st.session_state["inputs"])