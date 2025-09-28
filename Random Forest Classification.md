**Random Forest** is an **ensemble ML algorithm** that can be used for **both regression and classification** tasks:  [[ML-Intro]]

---
# Problem
A **single decision tree** can sometimes make **unstable or biased splits**.

- Example: If the tree splits first on "Sunny", it may wrongly predict "Go" even though other factors (like "Windy") are important.
    
- This makes the model sensitive to the dataset → a small change in data can give a very different tree.
    

---

#### 🌲 **Random Forest Solution**

- Instead of relying on **one tree**, Random Forest builds a **forest of many trees**.
    
- Each tree is trained on a **random subset** of the data and features (this is called **bagging**).
    
- For prediction:
    
    - In **classification**, each tree votes → the **majority class** wins.
        
    - In **regression**, it takes the **average of predictions**.
        

✅ This reduces bias, avoids overfitting, and gives more **robust and accurate results**.

## 🌲 Random Forest (Classification)

- **What it is**:  
    Random Forest is an **ensemble algorithm** that builds **many Decision Trees** (a "forest") and combines their predictions.
    
    - For **classification** → it takes a **majority vote** from all trees.
        
    - For **regression** → it takes the **average** of all trees’ predictions.
        

---

### 🔑 Key Ideas

1. **Bootstrapping (Bagging)**:  
    Each tree is trained on a random subset of the data (sampled with replacement).
    
2. **Feature Randomness**:  
    When splitting a node, each tree only looks at a random subset of features, not all features.  
    → This prevents one strong feature from dominating and makes trees more diverse.
    
3. **Voting**:  
    Each tree gives a classification, and the forest chooses the class with the most votes.
    

---

### ⚖️ Why Random Forest is Better than Single Decision Tree?

- A single tree can **overfit** (memorize training data).
    
- A forest of trees → reduces overfitting, increases stability, and usually gives **better accuracy**.
    
- Handles both **categorical and numerical features** well.
    
- Works well even if you have missing values or noisy data.
    

---

### 📊 Example (Classification)

Suppose we want to classify whether a student **Passes** or **Fails** based on:

- Study hours
    
- Sleep hours
    
- Attendance
    
- We train 100 trees.
    
- Each tree makes its own prediction (Pass/Fail).
    
- Random Forest → takes the **majority vote**.
    

So even if a few trees are wrong, the **forest as a whole** gives a reliable prediction.

----

# Code:
* [Code 1](RFT_01.py)

