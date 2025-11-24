# 📘 Pandas — Beginner-Friendly Guide

Pandas is a fast, powerful, and easy-to-use Python library for **data analysis and data manipulation**. It is one of the most important tools in data science and machine learning.

---

# 📌 What is Pandas?

**Pandas** is a Python library that helps you:

* Load data
* Clean data
* Modify data
* Analyze data
* Work with tables (just like Excel)

It is built on top of **NumPy** and is widely used in:

* Machine Learning
* Data Science
* Data Cleaning
* Data Visualization
* Finance and Business Analytics

---

# 📌 Installing Pandas

```bash
pip install pandas
```

Importing Pandas:

```python
import pandas as pd
```

---

# 📌 Core Data Structures in Pandas

## 1️⃣ **Series** — One-dimensional data

Example:

```python
s = pd.Series([10, 20, 30])
```

Output:

```
0    10
1    20
2    30
```

---

## 2️⃣ **DataFrame** — Two-dimensional table (rows & columns)

Example:

```python
data = {
    'Name': ['Nithin', 'Rahul'],
    'Age': [20, 22]
}
df = pd.DataFrame(data)
```

Output:

```
    Name   Age
0  Nithin   20
1  Rahul    22
```

---

# 📌 Reading Data Files

## ✔ Read CSV

```python
df = pd.read_csv('data.csv')
```

## ✔ Read Excel

```python
df = pd.read_excel('data.xlsx')
```

## ✔ Read JSON

```python
df = pd.read_json('data.json')
```

---

# 📌 Basic DataFrame Operations

## ✔ View first rows

```python
df.head()
```

## ✔ View last rows

```python
df.tail()
```

## ✔ Shape of data

```python
df.shape
```

## ✔ Column names

```python
df.columns
```

## ✔ Summary statistics

```python
df.describe()
```

---

# 📌 Selecting Data

## ✔ Select a column

```python
df['Name']
```

## ✔ Select multiple columns

```python
df[['Name', 'Age']]
```

## ✔ Select rows using index

```python
df.loc[0]
df.iloc[0]
```

---

# 📌 Filtering Data

```python
df[df['Age'] > 21]
```

Example:

```
     Name   Age
1   Rahul   22
```

---

# 📌 Adding and Removing Columns

## ✔ Add a column

```python
df['Score'] = [90, 85]
```

## ✔ Drop a column

```python
df = df.drop('Score', axis=1)
```

---

# 📌 Handling Missing Data

```python
df.isnull()
df.isnull().sum()
df.dropna()
df.fillna(0)
```

---

# 📌 Sorting Data

```python
df.sort_values('Age')
df.sort_values('Age', ascending=False)
```

---

# 📌 Grouping Data

```python
df.groupby('Age').mean()
```

---

# 📌 Merging & Joining Tables

```python
pd.merge(df1, df2, on='id')
```

---

# 📌 Exporting Data

```python
df.to_csv('output.csv', index=False)
df.to_excel('output.xlsx', index=False)
```

---

# 📌 Pandas in Machine Learning

Pandas is used to:

* Load datasets
* Clean missing values
* Normalize/transform data
* Select useful features
* Prepare data for ML algorithms

Example:

```python
df = pd.read_csv('train.csv')
df = df.dropna()
X = df[['Age', 'Salary']]
y = df['Purchased']
```

---

# 📌 Summary

* Pandas is essential for data analysis
* Uses Series (1D) and DataFrame (2D)
* Helps you clean, analyze, and manage data
* Works perfectly with NumPy and ML libraries

---