import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data_set={
    "study_time": [2, 4, 6, 8, 1, 3, 5, 7],
    "sleep_hours": [6, 7, 5, 6, 4, 5, 7, 8],
    "result": ["Fail", "Pass", "Pass", "Pass", "Fail", "Fail", "Pass", "Pass"]
}

df=pd.DataFrame(data_set)

x_axis=df[["study_time","sleep_hours"]].values
y_axis=df["result"].values 

# split the dataset into training and testing sets
train_x,test_x,train_y,test_y=train_test_split(x_axis,y_axis,test_size=0.1)

# Create a KNN model
model=KNeighborsClassifier(n_neighbors =3)

# Train the model
model.fit(train_x,train_y)

# Predict the result for a given study time and study 
input_study_time=int(input("Enter the study hours: "))
input_sleep_hours=int(input("Enter the sleep hours: "))
input_array=np.array([[input_study_time,input_sleep_hours]]).reshape(-1,2)

# predict the result
predicted_result=model.predict(input_array)
print(f"The predicted result is {predicted_result.item()}")

# predict the model accuracy
model_accuracy=model.score(test_x,test_y)
print(f"The model accuracy is {model_accuracy}")

