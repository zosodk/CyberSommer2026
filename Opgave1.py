# Opgave 1:
# Lav et script til at definere databasens tabelstruktur – hvis I har f.eks. to tabeller så også med en
# fremmednøgle. I skal bruge CREATE TABLE-kommandoen

# Import built-in sqlite3 library (comes with Python)
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("students.db")

# Create a cursor object
cursor = conn.cursor()

# Create a table - decide on a structure
cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    gender TEXT,
    birth_year INTEGER,
    has_former_degree INTEGER
)
""")

# We CAN represent boolean values by using the datatype integer and then clarify with the following
# in each value in column has_former_degree:
#
# 0 = False
# 1 = True

