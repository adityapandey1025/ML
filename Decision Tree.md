*It is also a supervised learning ML algorithm for classification as well as regression*[[ML-Intro]]

----

# Problem 
In our [model of girls’ nature](SVC_02.py), we have columns like **followers** and **following**. Since these values are very large, SVM tends to give more weight to them, while relatively smaller but more significant features such as **body count**, **late-night outings**, or **number of boyfriends** become less influential in the prediction.

For example, if a girl already has a **body count of 8+** or **6+ boyfriends**, she clearly falls into the _chinaar_ category — regardless of her followers, following count, or late-night talk hours. However, algorithms like **Linear Regression, KNN, and SVM** generally treat all numerical values proportionally, so large-scale features dominate the decision. This makes the model less effective.

👉 To address this, the **Decision Tree** algorithm was introduced, because it doesn’t rely on raw numerical magnitudes but rather splits based on **feature importance and thresholds** (e.g., _“if body count > 8 → chinaar”_), which better handles such cases.

Decion Tree works on following ways:->👇
![[Pasted image 20250927163600.png]]



# Understanding the Decision tree (How it Works ?)
_Below is the graph that shows how a **Decision Tree** works._

Consider the case of deciding whether a boy will go outside (explore nature) or not, depending on the **weather type**.

First, the model is trained on the given data. On the **top-right table**, we see the statistics:

- When the weather is **sunny**, he went outside **85 times** and stayed inside **0 times**. → This means if the day is sunny, he will definitely go outside.
    
- When the weather is **not sunny**, he went outside **30 times** and stayed inside **55 times**.
    

So, the next step is to check another condition — for example, whether it **rains** or not. Then, the decision process continues in the same way, splitting into branches until the model can classify the outcome accurately.

### Note -> A Decision Tree splits the dataset **step by step** using the most informative feature at each node (chosen by measures like **Gini Index** or **Entropy/Information Gain**).
![[Pasted image 20250927165756.png]]
## 1. **What is a Decision Tree?**

- A **supervised learning algorithm** used for **classification** and **regression**.
    
- It predicts the target variable by learning **simple decision rules from features**.
    
- Works like a **flowchart**:
    
    - **Root Node** → starting point (first question).
        
    - **Internal Nodes** → conditions on features (e.g., “Is age > 18?”).
        
    - **Branches** → outcomes of conditions (Yes/No).
        
    - **Leaf Nodes** → final predictions (class label or number).

```python
         Is age > 18?
         /         \
     Yes             No
    /                 \
 Pass Exam?         Fail Exam

```

## 2. **Why Decision Trees?**

- Earlier algorithms (Linear Regression, Logistic Regression, SVM) worked best when:
    
    - Data was **linearly separable**.
        
    - Features were **numerical only**.
        
- But real-world data is often **non-linear** and **mixed (numbers + categories)**.
    

👉 Decision Trees were developed to:

- Handle **non-linear data**.
    
- Be **interpretable** (easy to explain).
    
- Work with **mixed data types**.


## 3. **How does a Decision Tree work?**

At each node, the algorithm picks a feature and a condition that **best splits the data** into pure groups.

### Example:

Dataset: Students → Predict **Pass/Fail** based on Study Hours.
```Img
study_hours > 5 ?
   /        \
 Yes         No
Pass       Fail
```


---

## 4. **How does the tree choose where to split?**
:

![[Pasted image 20250927164134.png]]
## 5. **Advantages of Decision Trees**

✅ Easy to understand and interpret.  
✅ Handles **categorical + numerical data**.  
✅ No need for scaling/normalization.  
✅ Captures **non-linear relationships**.

---

## 6. **Disadvantages**

⚠️ Can **overfit** (make very deep trees).  
⚠️ Small changes in data → different tree (unstable).  
⚠️ Not the most accurate when used alone → better as **ensembles** (Random Forest, Gradient Boosting).

## 8. **When to Use Decision Trees**

- When **interpretability** is important.
    
- When data is **non-linear**.
    
- For quick prototyping.
    
- As base learners in **Random Forests & Gradient Boosting** (very powerful).
    

---

## 9. **Real-World Applications**

- Medical diagnosis (disease → yes/no).
    
- Credit scoring (approve/reject loan).
    
- Customer segmentation.
    
- Fraud detection.
    
- Churn prediction (leave/stay).

---
# Code
* [Code1](DT_01.py)
