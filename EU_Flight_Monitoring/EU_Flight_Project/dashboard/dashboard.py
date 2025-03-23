import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("EU Flight Monitoring Dashboard")

# Fetch all flights
st.header("All Flights")
flights = requests.get(f"{API_URL}/flights").json()
st.write(flights)

# Search by Airport
airport_code = st.text_input("Enter Airport Code (e.g., BER, FRA):")
if st.button("Search Flights"):
    airport_flights = requests.get(f"{API_URL}/flights/" + airport_code).json()
    st.write(airport_flights)

# Show Delayed Flights
st.header("Delayed Flights (> 2 hours)")
delayed_flights = requests.get(f"{API_URL}/flights/delayed").json()
st.write(delayed_flights)
