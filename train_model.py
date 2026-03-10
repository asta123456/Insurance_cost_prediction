import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle

# Load dataset
df = pd.read_csv("insurance.csv")

# Feature engineering
df["bmi_category"] = pd.cut(df["bmi"],
                            bins=[0,18.5,25,30,100],
                            labels=["Underweight","Normal","Overweight","Obese"])

df["age_group"] = pd.cut(df["age"],
                         bins=[0,30,50,100],
                         labels=["Young","Adult","Senior"])

df["smoker_bmi"] = df["bmi"] * (df["smoker"] == "yes")

# Convert categorical to numeric
df = pd.get_dummies(df, drop_first=True)

# Features and target
X = df.drop("charges", axis=1)
y = df["charges"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train,y_train)

# Predictions
pred = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test,pred)
rmse = np.sqrt(mean_squared_error(y_test,pred))
r2 = r2_score(y_test,pred)

print("MAE:",mae)
print("RMSE:",rmse)
print("R2 Score:",r2)

# Save model
pickle.dump(model,open("model.pkl","wb"))

print("Model saved successfully")