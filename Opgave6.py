# Et script til at tilføje én ny ”record” i databasen, baseret på input fra brugeren.
# I skal igen bruge INSERT INTO-kommandoen.
# Det vil være super hvis der var validering af hvert enkelt felt således at
# man ikke kan komme til at indsætte en tekst under et felt som kun kan indeholde tal.

#import sqlite3
from MyFunctions import DBConnector
# Opret forbindelse til databasen

conn = DBConnector()
cursor = conn.cursor()
try:
    while True:
        print("=== Opret ny studerende ===")

        # 1. Validering af navn (må ikke være tomt, skal have min. 2 tegn og må ikke indeholde tal)
        while True:
            name = input("Indtast fulde navn(eller 'Q' for at afslutte): ").strip()

            # Tjek om brugeren vil afslutte
            if name.lower() == "q":
                break

            if len(name) < 2:
                print("Fejl: Navnet skal indeholde mindst 2 tegn. Prøv igen.")
                continue

            # Tjek om der indgår tal i navnet (afviser f.eks. "34", "Peter2", osv.)
            if any(char.isdigit() for char in name):
            #checker hvert enkelt tegn og giver true, hvis der er et tal
                print("Fejl: Navnet må ikke indeholde tal. Prøv igen.")
                continue

            # Tjek at inputtet kun består af bogstaver, mellemrum eller bindestreg
            clean_name = name.replace(" ", "").replace("-", "")
            #clean-name placeholder for checks - beholder stadig name - blot til check med isalpha
            if not clean_name.isalpha():
                print("Fejl: Navnet må kun indeholde bogstaver, mellemrum og bindestreger. Prøv igen.")
                continue

            break
        # Hvis brugeren tastede 'Q', brydes den ydre løkke og programmet lukker
        if name.lower() == "q":
            print("\nAfslutter registrering...")
            break

        # 2. Validering af køn (kun specifikke tekstværdier tillades)
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
                gender = valid_genders[gender_input]
                break
            print("Fejl: Ugyldigt køn. Tast en af følgende: 'Male/mand', 'Female/kvinde' eller 'Other/anden'.")

        # 3. Validering af fødselsår (kun heltal i et fornuftigt interval)
        while True:
            birth_year_input = input("Indtast fødselsår (f.eks. 1999): ").strip()
            if not birth_year_input.isdigit():
                print("Fejl: Fødselsår skal bestå af tal (kun cifre). Prøv igen.")
                continue

            birth_year = int(birth_year_input)
            if 1900 <= birth_year <= 2026:
                break
            print("Fejl: Fødselsåret skal være mellem 1900 og 2026.")

        # 4. Validering af has_former_degree (kun 0 eller 1 som heltal)
        while True:
            former_degree_input = input("Har den studerende en tidligere uddannelse? (1 for Ja / 0 for Nej): ").strip()
            if former_degree_input in ("0", "1"):
                has_former_degree = int(former_degree_input)
                break
            print("Fejl: Feltet må kun indeholde tallet 0 eller 1.")

        # 5. Indsæt i databasen med INSERT INTO med cursor.execute()
        sql = """
        INSERT INTO students (name, gender, birth_year, has_former_degree)
        VALUES (?, ?, ?, ?);
        """

        cursor.execute(sql, (name, gender, birth_year, has_former_degree))
        conn.commit()

        # Vis bekræftelse
        new_id = cursor.lastrowid
        print(f"\nSucces! Studerende oprettet med ID {new_id}:")
        pass
finally:
    conn.close()
    print("Forbindelsen til databasen er lukket. Hav en god dag!")