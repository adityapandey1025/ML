import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split



study_time=np.array([20, 50, 32, 65, 23, 43, 10, 5, 22, 35, 29, 5, 56]).reshape(-1,1)
score=np.array([56, 83, 47, 93, 47, 82, 45, 78, 55, 67, 57, 4, 12]).reshape(-1,1)

# use 70% data for tarining model and use 30% data as testing the model
train_time,test_time,train_score,test_score=train_test_split(study_time,score,test_size=0.1)

model=LinearRegression()
model.fit(train_time,train_score)
input_time=int(input("Enter the study hours"))
result=model.predict([[input_time]])
print(f"The predicted score is {result}")

model_accuracy=model.score(test_time,test_score)
print(f"The model accuracy is {model_accuracy}")

# plotting the regression line
x_axis=np.linspace(0,70,100).reshape(-1,1)
plt.scatter(study_time,score,c='b',label='study time')
plt.plot(x_axis,model.predict(x_axis),'r--',label='Linear Regression function')
plt.scatter([input_time],[result.item()],label='Predicted score')
plt.legend(loc='upper left')
plt.show()

