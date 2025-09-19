import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the dataset
df=pd.read_csv("student_performance.csv")

# separate the input feature like study_time sleep_hours attendance practice_tests and output feature like score
study_time=df["study_time"].values.reshape(-1,1)
sleep_hours=df["sleep_hours"].values.reshape(-1,1)
attendance=df["attendance"].values.reshape(-1,1)
practice_test=df["practice_tests"].values.reshape(-1,1)
score=df["score"].values.reshape(-1,1)

# Create a Linear Regression model
model=LinearRegression()
x_dataset=np.concatenate((study_time,sleep_hours,attendance,practice_test),axis=1)
y_dataset=score

# Split the dataset into training and testing sets
train_x,test_x,train_y,test_y=train_test_split(x_dataset,y_dataset,test_size=0.2)

# Train the model
model.fit(train_x,train_y)

# Predict the score for a given set of study_time, sleep_hours, attendance, practice_test
input_study_time=int(input("Enter the study hours: "))
input_sleep_hours=int(input("Enter the sleep hours: "))
input_attendance=int(input("Enter the attendance percentage: "))
input_practice_test=int(input("Enter the practice test score: "))

input_array=np.array([[input_study_time,input_sleep_hours,input_attendance,input_practice_test]]).reshape(-1,4)
predicted_score=model.predict(input_array)
print(type(predicted_score))
print(f"The predicted score is {predicted_score.item()}")

# find the model accuracy
model_accuracy=model.score(test_x,test_y)
print(f"The model accuracy is {model_accuracy}")