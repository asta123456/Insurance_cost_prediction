import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl","rb"))

st.title("💊 Medical Insurance Cost Prediction")

st.write("Enter the details below to predict insurance charges")

age = st.slider("Age",18,65,25)

bmi = st.slider("BMI",10.0,50.0,25.0)

children = st.slider("Number of Children",0,5,0)

sex = st.selectbox("Gender",["male","female"])

smoker = st.selectbox("Smoker",["yes","no"])

region = st.selectbox("Region",
["southwest","southeast","northwest","northeast"])

# Convert categories
sex = 1 if sex=="male" else 0
smoker = 1 if smoker=="yes" else 0

if st.button("Predict Insurance Cost"):

    input_data = np.array([[age,bmi,children,sex,smoker]])

    prediction = model.predict(input_data)

    st.success(f"Estimated Insurance Cost: ${prediction[0]:.2f}")