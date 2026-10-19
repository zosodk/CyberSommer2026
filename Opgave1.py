# Et script til at definere databasens tabelstruktur – hvis I har f.eks. to tabeller så også med en
# fremmednøgle. I skal bruge CREATE TABLE-kommandoen

import sqlite3

# Create database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Define the structure of a table in the database
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

