# Et script til at læse og vise al data i tabellerne. Her bruges SELECT statementet. Data skal udskrives pænt i konsollen.
#
# Et script til at læse og vise data i tabellerne.

import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Get all the table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Loop through every table

for table in tables:
    table_name = table[0]  # Pulls the name out of the table

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    print(f"\n=== {table_name} ===") # Table header
    print([description[0] for description in cursor.description])  # Column names

    for row in rows:
        print(row)

conn.close()






