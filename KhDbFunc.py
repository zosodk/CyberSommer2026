import sqlite3
from sqlite3 import Error

def connect_to_db(db_name="students.db"):
    """
    Opretser og returnerer en forbindelse til SQLite databasen.
    returnerer en forbindelse til SQLite databasen, eller en fejl, hvis det ikke er muligt.
    """
    try:
        # opretter forbindelsen
        conn = sqlite3.connect(db_name)
        return conn
    except Error as e:
        print(f"Fejl ved forbindelse til databasen: {e}")
        return None

def create_table(conn):
    """
    Opret en tabel hvis den ikke allerede findes.
    """
    cursor = conn.cursor()
    # Eksempel på en tabel til studerende
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            gender TEXT,
            birth_year INTEGER,
            has_former_degree INTEGER
        )
    """)
    conn.commit()
    return cursor

def insert_student(conn, name, gender, birth_year, has_former_degree):
    """
    Indsætter en ny studerende i databasen.
    """
    cursor = conn.cursor()
    query = "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES (?, ?, ?, ?)"
    cursor.execute(query, (name, gender, birth_year, has_former_degree))
    conn.commit()
    print(f"Succes! {name} er tilføjet.")
    return cursor.lastrowid

def fetch_all_students(conn):
    """
    Henter alle studerende fra databasen.
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()


def validate_studentname() -> str:
    """
    Validates a student name. Whether the name is valid or not.
    :return:
    """
    while True:
        name = input("Indtast fulde navn(eller 'Q' for at afslutte): ").strip()

        # Tjek om brugeren vil afslutte
        if name.lower() == "q":
            return "q"

        if len(name) < 2:
            print("Fejl: Navnet skal indeholde mindst 2 tegn. Prøv igen.")
            continue

        # Tjek om der indgår tal i navnet (afviser f.eks. "34", "Peter2", osv.)
        if any(char.isdigit() for char in name):
            # checker hvert enkelt tegn og giver true, hvis der er et tal
            print("Fejl: Navnet må ikke indeholde tal. Prøv igen.")
            continue

        # Tjek at inputtet kun består af bogstaver, mellemrum eller bindestreg
        clean_name = name.replace(" ", "").replace("-", "")
        # clean-name placeholder for checks - beholder stadig name - blot til check med isalpha
        if not clean_name.isalpha():
            print("Fejl: Navnet må kun indeholde bogstaver, mellemrum og bindestreger. Prøv igen.")
            continue

        #navnet er godkent
        break
    return name

def validate_gender() -> str:
    """
    Validates the gender input. Whether the gender is valid or not.
    :return:
    """
    valid_genders = {
        "male": "Male",
        "mand": "Male",
        "female": "Female",
        "kvinde": "Female",
        "other": "Other",
        "anden": "Other"
    }
    while True:
        gender_input = input("Indtast køn (Male/mand/Female/kvinde(Other/anden): ").strip().lower()
        if gender_input in valid_genders:
            return valid_genders[gender_input]
        print("Fejl: Ugyldigt køn. Tast en af følgende: 'Male/mand', 'Female/kvinde' eller 'Other/anden'.")


def validate_birthyear() -> int:
    """
    Validates the birth year input. Whether the birth year is valid or not.
    """
    while True:
        birth_year_input = input("Indtast fødselsår (f.eks. 1999): ").strip()
        if not birth_year_input.isdigit():
            print("Fejl: Fødselsår skal bestå af tal (kun cifre). Prøv igen.")
            continue

        birth_year = int(birth_year_input)
        if 1900 <= birth_year <= 2026:
            return birth_year

        print("Fejl: Fødselsåret skal være mellem 1900 og 2026.")
def validate_degree() -> int:
    """
    Validates the degree input. Whether the degree is valid or not.
    """
    while True:
        degree_input = input("Har den studerende en tidligere uddannelse? (1 for Ja / 0 for Nej): ").strip()
        if degree_input in ("0", "1"):
            return int(degree_input)
        print("Fejl: Feltet må kun indeholde tallet 0 eller 1.")