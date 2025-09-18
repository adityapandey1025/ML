import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

time_studied = np.array([20, 50, 32, 65, 23, 43, 10, 5, 22, 35, 29, 5, 56]).reshape(-1, 1)
score = np.array([56, 83, 47, 93, 47, 82, 45, 78, 55, 67, 57, 4, 12]).reshape(-1,1)

model=LinearRegression()
model.fit(time_studied,score)
predict_value=np.array([45]).reshape(-1,1)
predcted_value=model.predict(predict_value)
print(predcted_value)

# plt.scatter() -> syntax 👇
# plt.scatter(x, y, s=size, c=color, marker='D', label='Training Data')
plt.scatter(time_studied,score,color='green',s=20,label='Training Data',marker='D')
plt.xlabel('Time')
plt.ylabel('Score')
plt.title('Linear Regression')
plt.legend(loc='upper left')  # moves the legend



# plt.plot() -> syntax👇
# plt.plot(x, y, c=color, marker='D', label='Training Data')
plt.plot(np.linspace(0,200,100).reshape(-1,1),model.predict(np.linspace(0,200,100).reshape(-1,1)),'r--')
plt.xlim([0,100])
plt.ylim([0,100])
plt.show()


