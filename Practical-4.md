# Practical 4: Python SQLite CRUD Operations

આ પ્રોજેક્ટ Python ના built-in `sqlite3` મોડ્યુલનો ઉપયોગ કરીને **CRUD (Create, Read, Update, Delete)** ઓપરેશન્સ અને **Parameterized Queries** દ્વારા SQL Injection સામે સુરક્ષાનું પ્રદર્શન કરે છે.

---

## 📌 Practical Steps

1. SQLite database connect કરવું (`college.db`).
2. `students` નામનું Table create કરવું.
3. Parameterized query દ્વારા data INSERT કરવો.
4. Data SELECT/READ કરવો.
5. Data UPDATE કરવો.
6. Data DELETE કરવો.
7. `commit()` અને `close()` નો ઉપયોગ કરવો.
8. Parameterized Queries દ્વારા SQL Injection નું risk ઘટાડવું.

---

## 💻 Source Code

```python
import sqlite3

# 1. Database connection
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# 2. Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")

# 3. CREATE (Insert Data)
cursor.execute("""
INSERT INTO students (name, age, course)
VALUES (?, ?, ?)
""", ("Parth", 17, "Computer Science & Engineering"))

conn.commit()
print("Data Inserted Successfully")

# 4. READ (Fetch Data)
cursor.execute("SELECT * FROM students")
students = cursor.fetchall()

print("\nStudent Records:")
for student in students:
    print(student)

# 5. UPDATE (Modify Data)
cursor.execute("""
UPDATE students
SET course = ?
WHERE id = ?
""", ("Information Technology", 1))

conn.commit()
print("\nData Updated Successfully")

# 6. DELETE (Remove Data)
cursor.execute("""
DELETE FROM students
WHERE id = ?
""", (1,))

conn.commit()
print("Data Deleted Successfully")

# 7. Close Connection
conn.close()
print("\nDatabase Connection Closed")
