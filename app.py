import streamlit as st
import pickle
import pandas as pd

# -------------------------------
# Load model
# -------------------------------
@st.cache_data
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("Insurance Cost Prediction")

# User inputs
age = st.number_input("Age", 18, 100, 30)
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
children = st.number_input("Number of Children", 0, 10, 0)
sex = st.selectbox("Sex", ["male", "female"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northwest", "northeast", "southwest", "southeast"])

# -------------------------------
# Encode inputs and match training features
# -------------------------------
# One-hot encode categorical variables
sex_encoded = 1 if sex == "male" else 0
smoker_encoded = 1 if smoker == "yes" else 0
region_encoded = {
    "northwest": [1,0,0,0],
    "northeast": [0,1,0,0],
    "southwest": [0,0,1,0],
    "southeast": [0,0,0,1]
}[region]

# Build DataFrame in exact column order
input_df = pd.DataFrame([[
    age,
    bmi,
    children,
    sex_encoded,
    smoker_encoded,
    *region_encoded
]], columns=model.feature_names_in_)  # <-- VERY IMPORTANT

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.success(f"Estimated Insurance Cost: ${prediction[0]:.2f}")
