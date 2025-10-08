A **Neural Network (NN)** is a machine learning model inspired by how the human brain processes information. It’s used for tasks like classification, regression, image recognition, speech recognition, and natural language processing.[[ML-Intro]]

---

## 🔑 Key Concepts of a Neural Network

### 1. **Neuron (Node)**

- Basic unit of a neural network.
    
- Each neuron takes inputs, applies weights, sums them, passes through an activation function, and produces an output.

![[Pasted image 20250928231916.png]]
### 2. **Layers**

- **Input layer** → Receives raw data (features).
    
- **Hidden layers** → Perform transformations/learning patterns.
    
- **Output layer** → Produces the final prediction (e.g., class label, probability).
    

---

### 3. **Weights & Bias**

- **Weights** → Strength of connections between neurons.
    
- **Bias** → Shifts the output of activation functions to improve learning.
    

---

### 4. **Activation Functions**

Introduce **non-linearity** so the model can learn complex patterns:

- **Sigmoid** → Squashes values between 0 and 1.
    
- **ReLU (Rectified Linear Unit)** → Replaces negative values with 0.
    
- **Softmax** → Used in output layer for classification.
    

---

### 5. **Forward Propagation**

Data flows from input → hidden layers → output, computing predictions.

---

### 6. **Loss Function**

Measures error between predicted output and true values. Examples:

- **MSE (Mean Squared Error)** for regression.
    
- **Cross-Entropy Loss** for classification.
    

---

### 7. **Backpropagation**

- Uses **gradient descent** to adjust weights and biases.
    
- Minimizes the loss by propagating errors backward.
    

---

### 8. **Training Process**

1. Initialize weights randomly.
    
2. Forward pass → compute output.
    
3. Compute loss.
    
4. Backpropagate error.
    
5. Update weights using optimization (e.g., SGD, Adam).
    
6. Repeat until model converges.