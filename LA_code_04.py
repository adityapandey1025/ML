import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the dataset
df=pd.read_csv("study_time_score_realistic.csv")

study_time=df["study_time"].values.reshape(-1,1)
score=df["score"].values

# split the dataset into training and testing sets

train_time,test_time,train_score,test_score=train_test_split(study_time,score,test_size=0.2)

# Create a Linear Regression model
model=LinearRegression()
model.fit(train_time,train_score)

# Predict the score for a given study time
input_time=int(input("Enter the study hours - > "))
input_array=np.array([[input_time]]).reshape(-1,1)
predicted_score=model.predict(input_array)
print(f"The predicted score is {predicted_score.item()}")


# Calculate the model accuracy
model_accuracy=model.score(test_time,test_score)
print(f"The model accuracy is {model_accuracy}")

#plot the regression line
plt.scatter(study_time,score,s=10,c="red",marker='*',label="Training data");
plt.plot(np.linspace(-20,80,100).reshape(-1,1),model.predict(np.linspace(-20,80,100).reshape(-1,1)),'g--',label="Regression line");
plt.scatter(input_array,[predicted_score.item()],s=30,c="black",marker='D',label="predicted value");
plt.xlim(-20,120)
plt.ylim(-20,120)
plt.legend()
plt.show()
