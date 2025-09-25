Support Vector Machines (SVM) is a **supervised ML learning algorithm** that can be used for both **classification** and **regression** tasks.[[ML-Intro]]

---
# Problem Setup

Suppose we have a graph with **two features** (`feature1` and `feature2`).

- We have **two categories**:
    
    - **Red points** (Category 1)
        
    - **Blue points** (Category 2)
        

Now, given a new/unknown point, we want to predict which category it belongs to.

---

### K-Nearest Neighbors (KNN) Approach

In the **KNN algorithm**, we look at the **k nearest neighbors** of the new point.

- If most of its neighbors belong to the red category, we classify it as **red**.
    
- If most belong to the blue category, we classify it as **blue**.
    

KNN works by **majority voting** among nearby points.

---

### How SVM is Different

In **SVM**, instead of looking at neighbors:

- We try to find an **optimal line (or hyperplane in higher dimensions)** that separates the two categories.
    
- This line is chosen so that the **margin (distance from the nearest points of each category to the line)** is as **wide as possible**.
    
- When a new/unknown point appears, its position relative to the line decides the category:
    
    - If it lies on one side → classify as **red**
        
    - If it lies on the other side → classify as **blue**


![[Pasted image 20250922222123.png]]


# 🧠 Support Vector Machines (SVM)

## 1. **What is SVM?**

- An algorithm for **classification** (mainly) and also **regression**.
    
- Idea: Find the **best boundary (hyperplane)** that separates different classes.
    
- Unlike Linear Regression or Logistic Regression, it focuses on **maximizing the margin** between classes.
    

👉 The goal = **separate classes with the widest possible “street” (margin).**

---

## 2. **Key Terms**

- **Hyperplane** → The decision boundary (line in 2D, plane in 3D, etc.).
    
- **Support Vectors** → Data points closest to the hyperplane; they define the margin.
    
- **Margin** → Distance between hyperplane and support vectors. SVM tries to maximize this.
    
- **Kernel** → A function that allows SVM to handle **non-linear data** by mapping it into higher dimensions.
    

---

## 3. **Types of SVM**

1. **Linear SVM**
    
    - Works when data is linearly separable.
        
    - Example: Separate Pass/Fail with straight line.
        
2. **Non-linear SVM (Kernel Trick)**
    
    - If data isn’t linearly separable, use kernels.
        
    - Common kernels:
        
        - **Linear** (default for linear problems).
            
        - **Polynomial** (curved boundaries).
            
        - **RBF (Radial Basis Function)** → most common for non-linear data.
            
        - **Sigmoid** (like neural nets).


## Why do we need hyperplanes 

In below case, it is impossible to draw a line or find a function of line which separate two category. That's why concept of hyperplanes(3D planes) are introduced......
*A **kernel** helps by transforming data into another space where separation is easier.*
![[Pasted image 20250922224316.png]]

## 7. **When to use SVM**

✅ Best for:

- Classification with **clear margins**.
    
- Works well with **small to medium datasets** (not millions).
    
- High-dimensional data (like text classification, bioinformatics).
    

⚠️ Not great when:

- Dataset is **very large** (training is slow).
    
- Lots of **noise** in data (SVM is sensitive).
    

---

## 8. **Project Examples**

- **Spam email classification** (spam / not spam).
    
- **Medical diagnosis** (disease present / not).
    
- **Handwriting recognition** (digits classification).
    
- **Face detection** (face vs non-face).


### Soft Margin
See We have two category one is red and another one is blue . There is blue line which seems to be possible but in SVM, we try to take those line which have max margin range between function line and support vectors points. So according to this yellowish line should be chosen. since it dont covered one each point for red and blue but still is the best function line for SVM...

![[Pasted image 20250922232055.png]]

