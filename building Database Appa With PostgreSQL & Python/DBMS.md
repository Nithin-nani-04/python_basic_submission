# 📘 Introduction to DBMS (Database Management System)

A **DBMS (Database Management System)** is software that is used to store, manage, retrieve, and organize data easily. It acts as a bridge between the user and the database.

---

# 📌 What Is DBMS?

A **DBMS** is a system that helps you:

* Store data in an organized form
* Retrieve data quickly
* Update data without errors
* Maintain data security
* Manage large datasets efficiently

Examples of DBMS:

* MySQL
* PostgreSQL
* Oracle
* SQL Server
* MongoDB (NoSQL)

---

# 📌 Why Do We Need a DBMS?

### ✔ To store large amounts of data

Data grows every second in companies, apps, and banks.

### ✔ To avoid duplication and errors

DBMS maintains accuracy using constraints and rules.

### ✔ To provide fast access

DBMS retrieves data within milliseconds.

### ✔ To keep data secure

Only authorized users can access or edit data.

### ✔ To support multiple users at the same time

Many users can access the system without crashing it.

---

# 📌 Components of DBMS

### 1. **Hardware**

Physical devices: computers, servers, storage.

### 2. **Software**

The DBMS application (MySQL, Oracle).

### 3. **Data**

Actual information stored in the system.

### 4. **Users**

* End Users
* Database Admins (DBA)
* Developers

### 5. **Procedures**

Instructions and rules for managing the database.

---

# 📌 Types of DBMS

### 1. **Relational DBMS (RDBMS)**

Stores data in tables (rows and columns).
Examples:

* MySQL
* PostgreSQL
* Oracle

### 2. **NoSQL DBMS**

Stores unstructured data.
Examples:

* MongoDB
* Cassandra
* Firebase

### 3. **Hierarchical DBMS**

Data is stored in a tree-like structure.
Example:

* IBM IMS

### 4. **Network DBMS**

Each record can have multiple parent-child relationships.

---

# 📌 DBMS Architecture (Simple Diagram)

```
+-----------------------+
|      End Users        |
+-----------+-----------+
            |
            v
+-----------------------+
|   DBMS Software       |
+-----------+-----------+
            |
            v
+-----------------------+
|      Database         |
+-----------------------+
```

---

# 📌 Key Features of DBMS

### ✔ Data Security

Protects data from unauthorized access.

### ✔ Data Independence

Changing storage does not affect user applications.

### ✔ Backup and Recovery

Restores data in case of failure.

### ✔ Data Consistency

Same data is maintained across the system.

### ✔ Multi-user Access

Many users can work simultaneously.

---

# 📌 Advantages of DBMS

* Reduces data redundancy
* Ensures data security
* Simplifies data management
* Improves data sharing
* Provides backup and recovery
* Supports ACID properties

---

# 📌 Disadvantages of DBMS

* Expensive to install and maintain
* High storage required
* Needs trained professionals

---

# 📌 ER Diagrams (Beginner-Friendly)

An **ER Diagram (Entity-Relationship Diagram)** visually represents how data is stored and how tables (entities) relate to each other.

## 📍 Basic Terms

### ✔ Entity

A real-world object (Student, Course, Product).

### ✔ Attribute

Details about an entity (name, age, price).

### ✔ Relationship

How entities are connected.

---

## 📍 Simple ER Diagram Example (Text-Based)

### Example: A School System

```
 +------------+         +-------------+         +---------------+
 |  STUDENT   |         |   ENROLLS   |         |    COURSE     |
 +------------+         +-------------+         +---------------+
 | student_id | <-----  | student_id  |  -----> | course_id     |
 | name       |         | course_id   |         | title         |
 | class      |         | date        |         | teacher       |
 +------------+         +-------------+         +---------------+
```

### Meaning:

* A **Student** enrolls in a **Course**.
* The **Enrolls** table acts as a link between student and course.

---

# 📌 Normalization (1NF → 3NF)

Normalization is the process of organizing data to reduce redundancy and improve consistency.

---

## ⭐ 1NF — First Normal Form

### Rules:

* No repeating groups
* Each cell must contain a single value
* Each record must be unique

### ❌ Not in 1NF

| student_id | name   | subjects      |
| ---------- | ------ | ------------- |
| 1          | Nithin | Math, Science |

### ✔ Converted to 1NF

| student_id | name   | subject |
| ---------- | ------ | ------- |
| 1          | Nithin | Math    |
| 1          | Nithin | Science |

---

## ⭐ 2NF — Second Normal Form

### Rules:

* Must be in 1NF
* No partial dependency (non-key attributes must depend on the full primary key)

### Example (Not in 2NF)

Composite Key → (student_id, course_id)

| student_id | course_id | student_name |
| ---------- | --------- | ------------ |
| 1          | 101       | Nithin       |

**Problem:** `student_name` depends only on `student_id`, not the full key.

### ✔ Converted to 2NF

**Students Table**

| student_id | student_name |
| ---------- | ------------ |
| 1          | Nithin       |

**Enrollment Table**

| student_id | course_id |
| ---------- | --------- |
| 1          | 101       |

---

## ⭐ 3NF — Third Normal Form

### Rules:

* Must be in 2NF
* No transitive dependency (non-key → non-key)

### Example (Not in 3NF)

| student_id | city      | pincode |
| ---------- | --------- | ------- |
| 1          | Bangalore | 560001  |

**Problem:** city → pincode (city depends on pincode, not student_id)

### ✔ Converted to 3NF

**Students Table**

| student_id | city      |
| ---------- | --------- |
| 1          | Bangalore |

**City Table**

| city      | pincode |
| --------- | ------- |
| Bangalore | 560001  |

---

# 📌 Summary

* DBMS helps in storing and managing data efficiently.
* It provides data security, consistency, and fast access.
* RDBMS uses tables; NoSQL handles unstructured data.
* DBMS is used in almost all modern applications.

---