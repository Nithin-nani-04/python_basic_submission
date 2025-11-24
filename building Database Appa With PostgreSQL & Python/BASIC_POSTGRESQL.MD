# 📘 Basic PostgreSQL — Beginner Friendly Guide

This file introduces **PostgreSQL**, one of the most powerful and popular open-source relational database systems. Perfect for beginners who want to learn SQL using PostgreSQL.

---

# 📌 What is PostgreSQL?

**PostgreSQL** (also called Postgres) is a free, open-source, relational database management system (RDBMS). It stores data in **tables** and uses **SQL** to manage and query data.

### ⭐ Features:

* Open-source & free
* Powerful and reliable
* Supports large datasets
* Works on Windows, Linux, macOS
* Supports advanced SQL features

---

# 📌 Installing PostgreSQL

You can install PostgreSQL from the official site:
👉 [https://www.postgresql.org/download](https://www.postgresql.org/download)

It comes with **pgAdmin**, a GUI tool to manage the database.

---

# 📌 Basic PostgreSQL Architecture (Simple Diagram)

```
 +-------------------------+
 |        User/App         |
 +------------+------------+
              |
              v
 +-------------------------+
 |    PostgreSQL Server    |
 +------------+------------+
              |
              v
 +-------------------------+
 |       Databases         |
 +-------------------------+
```

---

# 📌 Connecting to PostgreSQL

Once installed, open terminal and run:

```bash
psql -U postgres
```

`postgres` is the default username.

---

# 📌 Basic PostgreSQL Commands

## ✔ Show all databases

```sql
\l
```

## ✔ Create a new database

```sql
CREATE DATABASE school;
```

## ✔ Connect to a database

```sql
\c school;
```

## ✔ Show all tables

```sql
\dt
```

## ✔ Create a table

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT
);
```

## ✔ Insert data

```sql
INSERT INTO students (name, age)
VALUES ('Nithin', 20), ('Rahul', 22);
```

## ✔ Select data

```sql
SELECT * FROM students;
```

## ✔ Update data

```sql
UPDATE students
SET age = 23
WHERE id = 1;
```

## ✔ Delete data

```sql
DELETE FROM students WHERE id = 2;
```

---

# 📌 PostgreSQL Data Types (Beginner Level)

### 🔹 String Types

* `VARCHAR(n)`
* `TEXT`

### 🔹 Numeric Types

* `INT`
* `BIGINT`
* `SERIAL` (auto increment)

### 🔹 Date & Time

* `DATE`
* `TIMESTAMP`

### 🔹 Boolean

* `BOOLEAN` (true/false)

---

# 📌 Constraints in PostgreSQL

### ✔ PRIMARY KEY

Uniquely identifies a row.

```sql
id SERIAL PRIMARY KEY
```

### ✔ NOT NULL

Prevents empty values.

```sql
name VARCHAR(50) NOT NULL
```

### ✔ UNIQUE

Ensures no duplicate values.

```sql
email VARCHAR(100) UNIQUE
```

### ✔ FOREIGN KEY

Links two tables.

```sql
FOREIGN KEY (student_id) REFERENCES students(id)
```

---

# 📌 Simple ER Diagram Example

```
+-------------+      +-----------------
|  students   |      |    courses      |
+-------------+      +-----------------
| id (PK)     |<-----| student_id (FK) |
| name        |      | course_name     |
| age         |      | marks           |
+-------------+      +-----------------+
```

---

# 📌 How PostgreSQL Is Used in Projects

### ✔ Web applications

Django, Flask, Node.js, Spring Boot use PostgreSQL.

### ✔ Data analysis & ML

Datasets are stored in PostgreSQL → fetched for ML models.

### ✔ Banking & finance

Highly secure and ACID compliant.

### ✔ Enterprise systems

Reliable, scalable, and robust.

---

# 📌 Summary

* PostgreSQL is a relational database using SQL.
* Easy to use, highly secure, and completely free.
* Perfect for projects, data science, and backend apps.
* Supports all core SQL commands (CREATE, INSERT, SELECT, UPDATE, DELETE).

---
