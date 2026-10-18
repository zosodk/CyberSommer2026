# Et script til at definere databasens tabelstruktur – hvis I har f.eks. to tabeller så også med en
# fremmednøgle. I skal bruge CREATE TABLE-kommandoen

import sqlite3

# Create database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Define the structure of a table in the database
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    gender TEXT,
    birth_year INTEGER
)
""")

