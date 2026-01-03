import streamlit as st
import joblib

model = joblib.load("model/delay_cost_model.pkl")

st.title("SmartRoute+ 🚚")

distance = st.slider("Distance (km)", 1, 500)
traffic = st.selectbox("Traffic Level", ["Low","Medium","High"])
weather = st.selectbox("Weather", ["Clear","Rain","Fog"])
weight = st.slider("Package Weight (kg)", 1, 50)
slot = st.selectbox("Delivery Slot", ["Morning","Afternoon","Evening"])
fuel = st.slider("Fuel Cost per km", 5.0, 15.0)

encode = {"Low":0,"Medium":1,"High":2,
          "Clear":0,"Rain":1,"Fog":2,
          "Morning":0,"Afternoon":1,"Evening":2}

input_data = [[distance, encode[traffic], encode[weather], weight, encode[slot], fuel]]

if st.button("Predict"):
    result = model.predict(input_data)
    st.success(f"⏱️ Delay: {int(result[0][0])} minutes")
    st.success(f"💰 Cost: ₹{int(result[0][1])}")
