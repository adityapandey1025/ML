from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from sklearn.datasets import load_digits

# load the data
digits=load_digits()
print(digits.data)
model=KMeans(n_clusters=10,init='random',n_init=10)
model.fit(digits.data)

print(model.labels_)        # cluster assignments
print(model.cluster_centers_.shape)  # shape of cluster centers
print(model.inertia_)       # total within-cluster sum of squares
