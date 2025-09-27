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


