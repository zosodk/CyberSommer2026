# MyFunctions.py
import sqlite3


def DBConnector(db_file="students.db"):
    #Opretter og returnerer en forbindelse til SQLite-databasen
    try:
        conn = sqlite3.connect(db_file)
        #row_factory gør at resultaterne returneres som dictionaries og kan tilgås ved at bruge kolonnenavn som nøgler
        #i stedet for id numre (row[0] gjorde vi før - nu row["id"] eller row["name"] osv.)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Fejl ved forbindelsen til SQLite: {e}")
        return None