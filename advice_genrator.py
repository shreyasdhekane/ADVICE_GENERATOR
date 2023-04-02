import streamlit as st
import requests
import datetime
import smtplib


def get_random_advice(): #function to get advice
    response = requests.get('https://api.adviceslip.com/advice')
    if response.status_code == 200:
        data = response.json()
        return data['slip']['advice']
    else:
        return 'Failed to retrieve advice'
    
def get_advice_by_id(advice_id):# search function 
    response = requests.get(f'https://api.adviceslip.com/advice/{advice_id}')
    if response.status_code == 200:
        data = response.json()
        return data['slip']['advice']
    else:
        return 'Failed to retrieve advice'
    
st.set_page_config(page_title="Advice of the Day", page_icon=":memo:", layout="wide")

st.markdown("<h1 style='text-align: center;'><u>Advice of the day </u></h1>",unsafe_allow_html=True)
# Get the current date
now = datetime.date.today()
# Convert the current date to day of the year
day_of_year = now.timetuple().tm_yday

advice = get_advice_by_id(day_of_year)
st.markdown(f'<h2>{advice}</h2>', unsafe_allow_html=True)

now = datetime.datetime.now()

# Get the number of days elapsed in the current year
days_elapsed = (now - datetime.datetime(now.year, 1, 1)).days

# Get the total number of days in the current year
total_days = (datetime.datetime(now.year + 1, 1, 1) - datetime.datetime(now.year, 1, 1)).days

# Calculate the progress as a percentage
progress = int(days_elapsed / total_days * 100)

# Display the progress bar
st.progress(progress)
col3,col4=st.columns([20,1])
with (col3):
    st.markdown(f"<h5 style='text-align: left;'> {day_of_year} / 365 </h5>", unsafe_allow_html=True)
with (col4):
    st.markdown(f"<h5 style='text-align: left;'> {progress}% </h5>", unsafe_allow_html=True)

advice_id = st.text_input('Enter a number to search:', value='')
# Button to search for advice
col1, col2 = st.columns([5,1])
if col1.button('Search'):
    if advice_id:
        advice = get_advice_by_id(advice_id)
        st.markdown(f'<h2>{advice}</h2>', unsafe_allow_html=True)
    else :
        st.markdown(f'<h2>"Error 404: Advice not found. Please try again after consulting your nearest fortune teller."</h2>', unsafe_allow_html=True)

# Generate random advice
if col2.button('Generate Random Advice'):
    advice = get_random_advice()
    st.markdown(f'<h2>{advice}</h2>', unsafe_allow_html=True)
