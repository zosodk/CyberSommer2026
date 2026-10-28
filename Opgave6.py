# Et script til at tilføje én ny ”record” i databasen, baseret på input fra brugeren.
# I skal igen bruge INSERT INTO-kommandoen.
# Det vil være super hvis der var validering af hvert enkelt felt således at
# man ikke kan komme til at indsætte en tekst under et felt som kun kan indeholde tal.

#import sqlite3
from KhDbFunc import *

# Opret forbindelse til databasen

conn = connect_to_db("students.db")
if conn is None:
    print("Kunne ikke oprette forbindelse til databasen.")
    exit(1)

cursor = conn.cursor()
try:
    while True:
        print("=== Opret ny studerende ===")

        # 1. Validering af navn (må ikke være tomt, skal have min. 2 tegn og må ikke indeholde tal)
        name = validate_studentname()

        # Hvis brugeren tastede 'Q', brydes den ydre løkke og programmet lukker
        if name.lower() == "q":
            print("\nAfslutter registrering...")
            break

        # 2. Validering af køn (kun specifikke tekstværdier tillades)
        gender = validate_gender()

        # 3. Validering af fødselsår (kun heltal i et fornuftigt interval)
        birth_year = validate_birthyear()

        # 4. Validering af has_former_degree (kun 0 eller 1 som heltal)
        has_former_degree = validate_degree()

        # 5. Indsæt i databasen med INSERT INTO med cursor.execute()
        new_id = insert_student(conn, name, gender, birth_year, has_former_degree)

        conn.commit()

        # Vis bekræftelse

        print(f"\nSucces! Studerende oprettet med ID {new_id}:")
        pass
finally:
    conn.close()
    print("Forbindelsen til databasen er lukket. Hav en god dag!")