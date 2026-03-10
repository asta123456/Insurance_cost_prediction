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
st.write("Enter your details below:")

# -------------------------------
# User Input
# -------------------------------
age = st.number_input("Age", 18, 100, 30)
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
children = st.number_input("Number of Children", 0, 10, 0)
sex = st.selectbox("Sex", ["male", "female"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northwest", "northeast", "southwest", "southeast"])

# -------------------------------
# Preprocess Inputs
# -------------------------------
# Encode categorical variables
input_data = {
    'age': age,
    'bmi': bmi,
    'children': children,
    'sex': 1 if sex=="male" else 0,
    'smoker': 1 if smoker=="yes" else 0,
    # One-hot encode region
    'region_northwest': 1 if region=="northwest" else 0,
    'region_northeast': 1 if region=="northeast" else 0,
    'region_southwest': 1 if region=="southwest" else 0,
    'region_southeast': 1 if region=="southeast" else 0,
}

# Ensure all model features exist
for col in model.feature_names_in_:
    if col not in input_data:
        input_data[col] = 0  # fill missing features with 0

# Create DataFrame matching model features
input_df = pd.DataFrame([input_data], columns=model.feature_names_in_)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.success(f"Estimated Insurance Cost: ${prediction[0]:.2f}")
