import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

#load the dataset
data_set=load_iris()
print(data_set.keys())
print(data_set.feature_names)

# split the data
train_x,test_x,train_y,test_y=train_test_split(np.array(data_set.data),np.array(data_set.target),test_size=0.2)

clf1=DecisionTreeClassifier()
clf2=RandomForestClassifier()

clf1.fit(train_x,train_y)
clf2.fit(train_x,train_y)

print(f"The DT score is {clf1.score(test_x,test_y)}")
print(f"The RFT score is {clf2.score(test_x,test_y)}")

# plot the tree
plot_tree(clf1,feature_names=data_set.feature_names,class_names=data_set.target_names,filled=True,rounded=True)
plt.show()