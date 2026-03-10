import streamlit as st
import pickle
import pandas as pd

# -------------------------------
# Load the model
# -------------------------------
@st.cache_data(show_spinner=False)  # caches model so it loads once
def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("Insurance Cost Prediction")
st.write("Enter the details below to predict insurance cost:")

# -------------------------------
# User Input
# -------------------------------
age = st.number_input("Age", min_value=18, max_value=100, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
sex = st.selectbox("Sex", ["male", "female"])
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northwest", "northeast", "southwest", "southeast"])

# -------------------------------
# Preprocess Input (match training)
# -------------------------------
# Encode categorical variables exactly as in training
sex_encoded = 1 if sex == "male" else 0
smoker_encoded = 1 if smoker == "yes" else 0

region_encoded = {
    "northwest": [1,0,0,0],
    "northeast": [0,1,0,0],
    "southwest": [0,0,1,0],
    "southeast": [0,0,0,1]
}[region]

# Create input DataFrame matching training columns
input_df = pd.DataFrame([[
    age,
    bmi,
    children,
    sex_encoded,
    smoker_encoded,
    *region_encoded  # unpack region one-hot
]], columns=[
    'age', 'bmi', 'children', 'sex', 'smoker',
    'region_northwest', 'region_northeast', 'region_southwest', 'region_southeast'
])

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.success(f"Estimated Insurance Cost: ${prediction[0]:.2f}")
