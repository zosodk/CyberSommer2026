# Et script til at tilføje én ny ”record” i databasen, baseret på input fra brugeren.
# I skal igen bruge INSERT INTO-kommandoen.
# Det vil være super hvis der var validering af hvert enkelt felt således at
# man ikke kan komme til at indsætte en tekst under et felt som kun kan indeholde tal.

import sqlite3

# Opret forbindelse til databasen
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

print("=== Opret ny studerende ===")

# 1. Validering af navn (tekst, må ikke være tomt)
while True:
    name = input("Indtast fulde navn: ").strip()
    if len(name) >= 2:
        break
    print("Fejl: Navnet skal indeholde mindst 2 tegn. Prøv igen.")

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
print(f"- Navn: {name}")
print(f"- Køn: {gender}")
print(f"- Fødselsår: {birth_year}")
print(f"- Tidligere uddannelse: {'Ja (1)' if has_former_degree == 1 else 'Nej (0)'}")

conn.close()