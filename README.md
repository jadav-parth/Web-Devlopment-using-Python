# Python SQLite CRUD Operations (Practical 4)

This repository contains a simple Python script demonstrating basic **CRUD (Create, Read, Update, Delete)** operations using the built-in `sqlite3` database engine.

---

## 📌 Features & Steps Covered

1. **Database Connection:** Connects to or creates an SQLite database (`college.db`).
2. **Table Creation:** Creates a `students` table if it does not already exist.
3. **Data Insertion (Create):** Inserts student records using **Parameterized Queries** to prevent SQL Injection risks.
4. **Data Retrieval (Read):** Fetches and displays all records from the database.
5. **Data Modification (Update):** Updates the course details for a specific student ID.
6. **Data Removal (Delete):** Deletes a record from the table safely.
7. **Transaction Management:** Uses `conn.commit()` to save changes and `conn.close()` to securely terminate the connection.

---

## 🛠️ Prerequisites

* **Python 3.x** installed on your system.
* No external libraries required (`sqlite3` comes built-in with Python).

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
