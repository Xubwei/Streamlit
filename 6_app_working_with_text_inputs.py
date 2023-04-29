# Core Pkgs
import streamlit as st

# Text Input
fname = st.text_input("Enter Firstname",max_chars = 10)
st.title(fname)

# Text Input Hide Password
password = st.text_input("Enter Password",type='password')

# Text Area
message = st.text_area("Enter Message",height=100)
st.write(message)

# Numbers
number = st.number_input("Enter Number",1.0,25.0)

# Date Input
myappointment = st.date_input("Appointment")

# Time Input
mytime = st.time_input("My Time")






































