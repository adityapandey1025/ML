import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_breast_cancer

# Load the breast cancer dataset
data_set=load_breast_cancer()
print(data_set.keys())


# print(type(data_set))
# print(data_set.data)
# print(data_set.feature_names)
# print(data_set.target_names)
# print(data_set.DESCR)


# Split the dataset into training and testing sets
train_x,test_x,train_y,test_y=train_test_split(np.array(data_set.data),np.array(data_set.target),test_size=0.2)

model=KNeighborsClassifier(n_neighbors=3)
model.fit(train_x,train_y)

model_accuracy=model.score(test_x,test_y)
print(f"The model accuracy is {model_accuracy}")


# checking through right value
input_array = np.array([14.5, 20.1, 90.2, 600.3, 0.10, 0.20, 0.15, 0.08, 0.25, 0.07,
                        0.50, 1.20, 3.00, 40.0, 0.005, 0.03, 0.04, 0.02, 0.02, 0.005,
                        16.0, 25.0, 105.0, 800.0, 0.12, 0.35, 0.30, 0.12, 0.25, 0.08]).reshape(1, -1)

predicted_result=model.predict(input_array)
print(f"The predicted result is {data_set.target_names[predicted_result]}")