# Import built-in sqlite3 library (comes with Python)
import sqlite3

# Create database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()


# Opgave 3:
# Lav et script til at tømme tabellerne for data. Her bruges DELETE FROM kommandoen.

# Delete all data inside the students table without deleting the table itself
# cursor.execute('DELETE FROM students')
cursor.execute('DELETE FROM students')

# Commit the changes
conn.commit()

# Close the database
conn.close()