*It is an Unsupervised learning ML algorithm that partitions data into K clusters by minimizing the distance to cluster centroids.*

---
# 🧠 K-Means Clustering

---

## 1. **What is K-Means?**
![[Pasted image 20250928060209.png]]

- An **unsupervised learning algorithm** (no labels, only features).
    
- Goal → Group data into **K clusters** based on similarity.
    
- Each cluster has a **centroid** (mean position of all points in that cluster).
    
- Each data point belongs to the cluster with the nearest centroid (by distance, usually Euclidean).
    

👉 It’s basically “grouping similar things together.”

---

## 2. **Steps of K-Means Algorithm**

1. Choose the number of clusters K.
    
2. Randomly initialize K centroids.
    
3. Assign each point to the nearest centroid.
    
4. Update centroids = mean of all points in that cluster.
    
5. Repeat steps 3–4 until centroids stop moving (convergence).

![[Pasted image 20250928060446.png]]

## 5. **How to choose K?**

Use the **Elbow Method**:

- Run KMeans for different values of K.
    
- Plot WCSS (error) vs. K.
    
- The “elbow point” (where curve bends) is the best K.
    

---

## 6. **Advantages**

✅ Simple, fast, and easy to implement.  
✅ Works well for spherical, evenly sized clusters.  
✅ Scales to large datasets.

---

## 7. **Limitations**

⚠️ Must choose K beforehand.  
⚠️ Sensitive to initial centroids (may converge to local minima).  
⚠️ Struggles with non-spherical clusters, different densities, or outliers.

---

## 8. **Real-World Applications**

- Customer segmentation (group by buying behavior).
    
- Market basket analysis.
    
- Image compression (group pixels into color clusters).
    
- Anomaly detection (points far from any cluster).

----

# Code
* [Code1](Kcluster_01.py)
* [Code2](Kcluster_02.py)
* 