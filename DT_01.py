import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split


# Load the dataset
data_set=load_breast_cancer()
print(data_set.keys())

# SPlit the dataset
train_x,test_x,train_y,test_y=train_test_split(np.array(data_set.data),np.array(data_set.target))

clf1=KNeighborsClassifier(n_neighbors=5)
clf1.fit(train_x,train_y)

clf2=SVC(kernel='linear',C=4)
clf2.fit(train_x,train_y)

clf3=DecisionTreeClassifier()
clf3.fit(train_x,train_y)

clf4=RandomForestClassifier()
clf4.fit(train_x,train_y)

print(f"Model accuracy of KNN is {clf1.score(test_x,test_y)}")
print(f"Model accuracy of SVC is {clf2.score(test_x,test_y)}")
print(f"Model accuracy of DT is {clf3.score(test_x,test_y)}")
print(f"Model accuracy of RFT is {clf4.score(test_x,test_y)}")

input = np.array([
    17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.0787,
    1.095, 0.9053, 8.589, 153.4, 0.0064, 0.049, 0.0537, 0.0159, 0.0300, 0.0062,
    25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119, 0.2654, 0.4601, 0.1189
]).reshape(1, -1)

DT_predict_value=clf3.predict(input)
RF_predict_value=clf3.predict(input)
print("The predicted result by DT is ",data_set.target_names[DT_predict_value])
print("The predicted result by RF is ",data_set.target_names[RF_predict_value])

# plot the decision tree
plot_tree(clf3,feature_names=data_set.feature_names, class_names=data_set.target_names, filled=True, rounded=True)
plt.show()