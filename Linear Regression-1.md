*It is the machine learning algorithm from supervised learning category* [[ML-Intro]]

---
#### Problem
In Supervised learning, We have lot of data . There is as large as input and for every input there is corresponding output. 
A Student score vs time he studied graph is given below -> 
![[Pasted image 20250918183922.png]]

In above Graph, There is input and output too. If we will have to predict the score from time I studies then my machine learing model should know the relation between input and output .
One of the easiest way to find relation is finding function between input x and output y.
So  Ml model should know that function. There is my algorithm to solve the above case . But one of easy algo , we will learn here is *Linear Regression*.

---
## 1. What is Linear Regression?

It’s one of the simplest ML algorithms.  
It tries to find a **straight-line relationship** between input(s) (features) and output (target).

**Equation (for one input feature):**

y=mx+cy = m x + cy=mx+c

- xxx: input feature (independent variable)
    
- yyy: output value (dependent variable)
    
- mmm: slope (tells how much yyy changes when xxx increases by 1)
    
- ccc: intercept (value of yyy when x=0x = 0x=0)
    

---

## 2. Types of Linear Regression

1. **Simple Linear Regression**
    
    - Only 1 input feature (like predicting weight based on height).
        
2. **Multiple Linear Regression**
    
    - More than 1 input feature (like predicting house price based on size, number of rooms, location, etc.).
        
    - Equation:
        
    
    y=b0+b1x1+b2x2+⋯+bnxny = b_0 + b_1x_1 + b_2x_2 + \dots + b_nx_ny=b0​+b1​x1​+b2​x2​+⋯+bn​xn​

---

## 3. How does the model learn?

We want the line to be as close as possible to the actual data points.

- The **difference** between the predicted value (y^\hat{y}y^​) and the actual value (yyy) is called **error** (or residual).
    
![[Pasted image 20250918185037.png]]


![[Pasted image 20250918184447.png]]
here in example, the red line is predicted function using Linear Regression . The diffrence between green dot and red line(corresponding value of time studied of green dot) is Error .

---

## 4. How do we minimize error?

![[Pasted image 20250918185107.png]]

---

## 5. Assumptions of Linear Regression

Linear regression works best when:

1. Relationship between input and output is linear.
    
2. Errors (residuals) are normally distributed.
    
3. No multicollinearity (features not highly correlated with each other).
    
4. Homoscedasticity (variance of errors is constant).
    

---

## 6. Example

Say we want to predict **house price** based on **size (sq.ft)**.

- Data:  
    (1000 sq.ft → $200k),  
    (1500 sq.ft → $300k),  
    (2000 sq.ft → $400k).
    

A linear regression model would learn something like:

![[Pasted image 20250918185427.png]]

# Example of Linear Regression
* *Predicting the score based on previous study time and score dataset*
	* [Basic code](LA_code_intro.py)
	* [Intermediate code](LA_code1.py)
	* [Model accuracy test code](LA_code_3.py)
	* [Data from csv file](LA_code_04.py)

# Example of Multiple Linear Regression
* *Predicting the score based on previous study time ,sleep time, attendance,practice test and score*
	* [Basic code](MR_code1.py)
* *Predicting the score based on previous study time and score dataset*
	* [code](MR_code2.py)

