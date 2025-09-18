import numpy as np
import matplotlib.pyplot as plt
from pygments.styles.dracula import green
from sklearn.linear_model import LinearRegression

study_time=np.array([20, 50, 32, 65, 23, 43, 10, 5, 22, 35, 29, 5, 56]).reshape(-1,1)
score=np.array([56, 83, 47, 93, 47, 82, 45, 78, 55, 67, 57, 4, 12]).reshape(-1,1)

model=LinearRegression()
model.fit(study_time,score)

input_time=int(input("Enter the time(in hr) of study time:"))
input_array = np.array([[input_time]]).reshape(-1,1)
predicted_score=model.predict(input_array)
print(predicted_score)

# Scatter effect
plt.scatter(study_time,score,s=25,c='green',marker='*',label='Score')
plt.xlabel('Study time')
plt.ylabel('Score')
plt.title('Linear Regression')
plt.legend(loc='upper left')

#plotting
plt.plot(np.linspace(0,80,100).reshape(-1,1),model.predict(np.linspace(0,80,100).reshape(-1,1)),'b--')
plt.scatter(input_array,predicted_score,s=50,color='red',marker='D',label='Predicted Score')
plt.plot([input_time,input_time],[0,predicted_score.item()],'g--')
plt.plot([0,input_time],[predicted_score.item(),predicted_score.item()],'g--')
plt.legend(loc='upper left')

plt.show()
