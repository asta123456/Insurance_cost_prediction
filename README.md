# Medical Insurance Cost Prediction

## 📌 Project Overview

This project predicts **medical insurance charges** based on personal and health-related attributes such as age, BMI, number of children, smoking status, and region.

A **Machine Learning model (Linear Regression)** is used to estimate the insurance cost.
The project also includes a **Streamlit web application** that allows users to enter their details and get a predicted insurance cost.

---

## 🎯 Objective

The goal of this project is to:

* Build a machine learning model to predict medical insurance charges.
* Perform feature engineering to improve prediction.
* Evaluate model performance using regression metrics.
* Deploy the model using a **Streamlit user interface**.

---

## 📊 Dataset

Dataset used: **Medical Cost Personal Dataset**

Features in the dataset:

* **age** – Age of the person
* **sex** – Gender (male/female)
* **bmi** – Body Mass Index
* **children** – Number of children covered by insurance
* **smoker** – Smoking status (yes/no)
* **region** – Residential region
* **charges** – Medical insurance cost (target variable)

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* GitHub

---

## ⚙️ Machine Learning Model

Model used:

* **Linear Regression**

Steps involved:

1. Load dataset using Pandas
2. Feature engineering
3. Train-test split
4. Train Linear Regression model
5. Evaluate using:

   * MAE (Mean Absolute Error)
   * RMSE (Root Mean Square Error)
   * R² Score
6. Save trained model using Pickle

---

## 🖥 Streamlit Web Application

A user-friendly web interface was created using **Streamlit** where users can:

* Enter age
* Enter BMI
* Select gender
* Enter number of children
* Select smoker status
* Select region

The app then predicts the **estimated insurance cost**.

---

## 📂 Project Structure

```
insurance_project
│
├── app.py
├── train_model.py
├── insurance.csv
├── model.pkl
├── requirements.txt
└── README.md
```

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```
python -m pip install -r requirements.txt
```

### 2️⃣ Train the Model

```
python train_model.py
```

### 3️⃣ Run the Streamlit App

```
python -m streamlit run app.py
```

---

## 🚀 Deployment

The project is deployed using **Streamlit Community Cloud**.

Steps:

1. Push project to GitHub
2. Connect repository to Streamlit Cloud
3. Deploy the `app.py` file

---

## 📈 Output

The application predicts **medical insurance cost** based on user inputs and displays the estimated charge instantly.

---

## 👩‍💻 Author

Asta Lakshmi
