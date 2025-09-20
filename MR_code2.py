import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# load the dataset
df=pd.read_csv("muthhi.csv")

x_data=df[["study_time","sleep_hours","attendance","muthhi"]].values
y_data=df["score"].values

# split the dataset into training and testing sets
train_x,test_x,train_y,test_y=train_test_split(x_data,y_data,test_size=0.2)

# Create a Linear Regression model
model=LinearRegression()
model.fit(train_x,train_y)

input_study_time=int(input("Enter the study hours: "))
input_sleep_hours=int(input("Enter the sleep hours: "))
input_attendance=int(input("Enter the attendance percentage: "))
input_muthhi=int(input("Enter the Muthhi in a day: "))

input_array=np.array([[input_study_time,input_sleep_hours,input_attendance,input_muthhi]]).reshape(-1,4)
predicted_result=model.predict(input_array)
print(f"The predicted score is {predicted_result.item()}")
if(predicted_result.item()<70):
    print("Muthhii kam maar basdk")
model_accuracy=model.score(test_x,test_y)
print(f"The model accuracy is {model_accuracy}")

