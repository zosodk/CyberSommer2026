# Et script til at læse og vise al data i tabellerne. Her bruges SELECT statementet. Data skal udskrives pænt i konsollen.
#
# Et script til at læse og vise data i tabellerne.

import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Get all the table names
cursor.execute("SELECT * FROM students;")
students = cursor.fetchall()

# Loop through every table

for student in students:
    print(student)
    print(f"\n=== studenter ===") # Table header



conn.close()






