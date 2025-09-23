import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

data_set=load_breast_cancer()


X_label=np.array(data_set.data)
y_label=np.array(data_set.target)
train_x,test_x,train_y,test_y=train_test_split(X_label,y_label,test_size=0.2,random_state=21)

# Adding SVM classifiers
clf=SVC(kernel='linear',C=5)
clf.fit(train_x,train_y)

model_accuracy1=clf.score(test_x,test_y)
print(f"The SVM  model accuracy is {model_accuracy1}")

# Adding KNN classifiers
clf=KNeighborsClassifier(n_neighbors=3)
clf.fit(train_x,train_y)

model_accuracy=clf.score(test_x,test_y)

print(f"The SVM  model accuracy is {model_accuracy1}")
print(f"The KNN model accuracy is {model_accuracy}")