import numpy as np
from scipy import cluster
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Use the function make_blobs which is used to create fake cluster data
X,y=make_blobs(n_samples=300,centers=4,cluster_std=0.9,random_state=42)

# clustering
kmeans=KMeans(n_clusters=4,random_state=42)
y_pred=kmeans.fit_predict(X)

# plot the graph
plt.scatter(X[:,0],X[:,1],c=y_pred,cmap='rainbow')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=20,c='black',marker='X')
plt.show()