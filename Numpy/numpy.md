# 📘 NumPy — Beginner-Friendly Guide

NumPy (**Numerical Python**) is the foundation of scientific computing and data analysis in Python. It provides fast and powerful tools to work with arrays, matrices, and mathematical operations.

---

# 📌 What is NumPy?

**NumPy** is a Python library used for:

* Working with large numerical datasets
* Performing mathematical operations
* Handling multi-dimensional arrays
* Fast computation (much faster than Python lists)

It is used in:

* Machine Learning
* Data Science
* Deep Learning
* Image Processing
* Scientific Research

---

# 📌 Why Use NumPy?

### ✔ Faster than Python lists

NumPy uses optimized C code internally.

### ✔ Supports multi-dimensional arrays

1D, 2D, 3D… arrays for data and images.

### ✔ Powerful mathematical functions

Mean, sum, std, linear algebra, etc.

### ✔ Basis for ML libraries

Pandas, TensorFlow, PyTorch all depend on NumPy.

---

# 📌 Installing NumPy

```bash
pip install numpy
```

Importing NumPy:

```python
import numpy as np
```

---

# 📌 Creating Arrays

### 1. From a Python list

```python
arr = np.array([1, 2, 3])
```

### 2. 2D Array

```python
arr2 = np.array([[1, 2], [3, 4]])
```

### 3. Using built-in functions

```python
np.zeros((3, 3))   # 3x3 matrix of zeros
np.ones((2, 2))    # matrix of ones
np.arange(1, 10)   # 1 to 9
np.linspace(0, 1, 5)  # 5 numbers between 0 and 1
```

---

# 📌 Array Attributes

```python
arr.shape     # dimensions
arr.ndim      # number of dimensions
arr.size      # total elements
arr.dtype     # data type
```

Example:

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
```

```
Shape: (2, 3)
Dimensions: 2
Size: 6
Data type: int64
```

---

# 📌 Indexing and Slicing

### Indexing

```python
arr[0]       # first element
arr[1, 2]    # row 1, column 2
```

### Slicing

```python
arr[0:2]       # first two elements
arr[:, 1]      # entire second column
```

---

# 📌 Basic Operations

```python
arr + 2        # element-wise
arr * 3
arr1 + arr2
np.sum(arr)
np.mean(arr)
np.max(arr)
np.min(arr)
```

---

# 📌 Reshaping Arrays

```python
arr.reshape(3, 2)
```

Example:

```
[1 2 3 4 5 6] → [[1 2], [3 4], [5 6]]
```

---

# 📌 Useful Functions

```python
np.unique(arr)
np.sort(arr)
np.dot(a, b)         # matrix multiplication
np.transpose(arr)
```

---

# 📌 Working With Random Numbers

```python
np.random.rand(3, 3)   # random values
np.random.randint(1, 10, 5)  # random integers
```

---

# 📌 NumPy in Machine Learning

NumPy is used to:

### ✔ Store datasets

### ✔ Perform vectorized operations

### ✔ Compute gradients

### ✔ Handle image arrays

### ✔ Build ML algorithms (mathematically)

Example:

```python
weights = np.random.randn(3, 3)
output = np.dot(weights, input_vector)
```

---

# 📌 Summary

* NumPy is essential for numerical computing in Python.
* Provides fast operations on arrays and matrices.
* Basis for ML, DL, Data Science libraries.
* Easy to use and extremely powerful.

---
