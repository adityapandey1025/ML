import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


# Load dataset
df=pd.read_csv('nature.csv')

#encode the late_night_out
night_out_encoder=LabelEncoder()
df["late_night_out"]=night_out_encoder.fit_transform(df["late_night_out"])

# Encode target 'category'
category_encoder = LabelEncoder()
df["category"] = category_encoder.fit_transform(df["category"])

X_label=df.drop(["category","id","name"],axis=1)
y_label=df["category"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_label)

# Train-test split
train_x,test_x,train_y,test_y=train_test_split(X_scaled,y_label,test_size=0.2)

# Train SVC
model=SVC(kernel="linear",C=5)
model.fit(train_x,train_y) 

# model accuracy
accuracy=model.score(test_x,test_y)
print(f"Model Accuracy: {accuracy}")

# Mapping dictionary for user-friendly input
night_out_map=["yes","no"]

user_input = {}
user_input["body_count"] = int(input("Enter body count: "))
user_input["followers"] = int(input("Enter instagram followers: "))
user_input["following"] = int(input("Enter instagram following: "))
user_input["late_talks_hours"] = int(input("Enter late talks hours with a friend or bf: "))
user_input["best_friends_count"] = int(input("Enter best friends count: "))
user_input["boyfriend_count"] = int(input("Enter boyfriend count: "))
user_input["late_night_out"] = input(f"Enter late night out ({'/'.join(night_out_map)}): ").lower()

# Convert input to dataframe
input_df = pd.DataFrame([user_input])

# Align input columns with training columns
input_df["late_night_out"] = night_out_encoder.transform(input_df["late_night_out"])
input_df = input_df.reindex(columns=X_label.columns, fill_value=0)

# Predict
predicted_result = model.predict(input_df)
predicted_category = category_encoder.inverse_transform(predicted_result)
print(f"The predicted category is: {predicted_category[0]}")

