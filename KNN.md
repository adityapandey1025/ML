*It is also a ML algorithm from supervised learning category*[[ML-Intro]]

---

## Problem
Suppose we have a graph of weight and height of different person and we classify some of them as skinny , fat and normal people . Its an example of supervised learning because in the dataset we already  tell that red one is fat and green is normal and blue is skinny. What our ML model predict ? It predicts the new data based point on the **majority class of its nearest neighbors**. It tells whether the new point is skinny or fat

![[Pasted image 20250921083105.png]]

## 🟢 Step 1: What is KNN?

- **KNN is a supervised ML algorithm used for classification (and regression).**
    
- It predicts the class of a new data point based on the **majority class of its nearest neighbors**.
    
- “Nearest” is measured using a **distance metric** (like Euclidean distance).
    

Example:  
If most of your friends who study 5 hours/day pass an exam, and you study 5 hours/day → KNN predicts you will also pass. ✅

---

## 🟢 Step 2: How does it work?

1. Choose a value of **K** (e.g., 3, 5, 7).
    
2. Calculate the **distance** between the new data point and all points in the training set.
    
    - Euclidean distance is most common:
        ![[Pasted image 20250921083839.png]]
        
1. Find the **K nearest neighbors**.
    
2. Use **majority voting** among those neighbors’ labels.
    
3. Assign the most frequent label as the prediction.
## 🟢 Step 3: Choosing K

- Small K (like 1, 3) → very sensitive to noise.
    
- Large K (like 15, 20) → smoother predictions but may blur class boundaries.
    
- Rule of thumb: **odd K** to avoid ties, and often tested with cross-validation.
    

---

## 🟢 Step 4: Example (conceptual)

Dataset: Fruit classification

- Features: Weight, Color score
    
- Labels: Apple, Orange
    

New fruit → (Weight=160, Color=6)

- Find nearest neighbors in dataset.
    
- If 4 are Apple, 1 is Orange → prediction = **Apple 🍎**.


# Examples of KNN
* [*KNN model on pass /fail*](KNN_01.py)
* [*KNN model on breast cancer dataset](KNN_02.py)
* [*KNN model on dating](KNN_03.py)
* 
	