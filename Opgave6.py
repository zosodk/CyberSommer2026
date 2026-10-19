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
    print("Fejl: Ugyldigt køn. Vælg 'Male/mand', 'Female(kvinde' eller 'Other/anden'.")