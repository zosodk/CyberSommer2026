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


# Opgave 2:
# Lav et script til ”bulk-insert” af 100, 500 eller måske endnu flere data. Her må/skal I bruge en LLM til at
# generere nogle kunstige data – bed LLM’en om at give Jer f.eks. 100 INSERT INTO-statements som
# passer til Jeres datamodel.

# For practical reasons we decided to create a list which contains all the SQL inter-into statements generated
# by AI and then execute them in another line, in a for loop

sql_statements = [
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Anna Jensen', 'Female', 1998, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Peter Nielsen', 'Male', 1995, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Maria Hansen', 'Female', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Lars Pedersen', 'Male', 1997, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Emma Andersen', 'Female', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Mikkel Christensen', 'Male', 1999, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Sofie Larsen', 'Female', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Frederik Sørensen', 'Male', 1994, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Laura Rasmussen', 'Female', 2003, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Jonas Jørgensen', 'Male', 1998, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Ida Jensen', 'Female', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Mathias Nielsen', 'Male', 1996, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Julie Hansen', 'Female', 1999, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Magnus Pedersen', 'Male', 1997, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Clara Andersen', 'Female', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Oliver Christensen', 'Male', 1995, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Sarah Larsen', 'Female', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Lucas Sørensen', 'Male', 2004, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Amalie Rasmussen', 'Female', 1998, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Victor Jørgensen', 'Male', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Katrine Jensen', 'Female', 1996, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Andreas Nielsen', 'Male', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Maja Hansen', 'Female', 2003, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Rasmus Pedersen', 'Male', 1997, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Nanna Andersen', 'Female', 1999, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Jakob Christensen', 'Male', 1995, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Line Larsen', 'Female', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Simon Sørensen', 'Male', 1998, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Camilla Rasmussen', 'Female', 2001, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Sebastian Jørgensen', 'Male', 1996, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Helene Jensen', 'Female', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Daniel Nielsen', 'Male', 1994, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Victoria Hansen', 'Female', 2004, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Alexander Pedersen', 'Male', 1999, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Louise Andersen', 'Female', 1998, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Christian Christensen', 'Male', 1997, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Cecilie Larsen', 'Female', 2003, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Martin Sørensen', 'Male', 2001, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Josefine Rasmussen', 'Female', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Emil Jørgensen', 'Male', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Thea Jensen', 'Female', 1999, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Noah Nielsen', 'Male', 2004, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Alma Hansen', 'Female', 2005, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('William Pedersen', 'Male', 1998, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Ella Andersen', 'Female', 2003, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Malte Christensen', 'Male', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Asta Larsen', 'Female', 2002, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Valdemar Sørensen', 'Male', 1997, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Frida Rasmussen', 'Female', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('August Jørgensen', 'Male', 1999, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Anna Nielsen', 'Female', 1997, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Peter Hansen', 'Male', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Maria Pedersen', 'Female', 2002, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Lars Andersen', 'Male', 1996, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Emma Christensen', 'Female', 2004, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Mikkel Larsen', 'Male', 1998, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Sofie Sørensen', 'Female', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Frederik Rasmussen', 'Male', 1995, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Laura Jørgensen', 'Female', 1999, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Jonas Jensen', 'Male', 2003, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Ida Nielsen', 'Female', 2001, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Mathias Hansen', 'Male', 1997, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Julie Pedersen', 'Female', 2005, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Magnus Andersen', 'Male', 1996, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Clara Christensen', 'Female', 1998, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Oliver Larsen', 'Male', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Sarah Sørensen', 'Female', 2001, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Lucas Rasmussen', 'Male', 2004, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Amalie Jørgensen', 'Female', 1999, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Victor Jensen', 'Male', 2000, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Katrine Nielsen', 'Female', 2003, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Andreas Hansen', 'Male', 1995, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Maja Pedersen', 'Female', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Rasmus Andersen', 'Male', 1998, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Nanna Christensen', 'Female', 1997, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Jakob Larsen', 'Male', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Line Sørensen', 'Female', 2004, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Simon Rasmussen', 'Male', 1999, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Camilla Jørgensen', 'Female', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Sebastian Jensen', 'Male', 1996, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Helene Nielsen', 'Female', 2003, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Daniel Hansen', 'Male', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Victoria Pedersen', 'Female', 1998, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Alexander Andersen', 'Male', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Louise Christensen', 'Female', 1997, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Christian Larsen', 'Male', 2000, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Cecilie Sørensen', 'Female', 2004, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Martin Rasmussen', 'Male', 1999, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Josefine Jørgensen', 'Female', 2002, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Emil Jensen', 'Male', 1998, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Thea Nielsen', 'Female', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Noah Hansen', 'Male', 2003, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Alma Pedersen', 'Female', 2005, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('William Andersen', 'Male', 1997, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Ella Christensen', 'Female', 1999, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Malte Larsen', 'Male', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Freja Madsen', 'Female', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Nikolaj Thomsen', 'Male', 1998, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Caroline Poulsen', 'Female', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Mads Knudsen', 'Male', 1997, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Stine Mortensen', 'Female', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Jesper Holm', 'Male', 1999, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Pernille Dahl', 'Female', 2003, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Henrik Lund', 'Male', 1994, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Louisa Vestergaard', 'Female', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Benjamin Kristensen', 'Male', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Signe Bach', 'Female', 1998, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Tobias Eriksen', 'Male', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Mille Gregersen', 'Female', 2004, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Casper Kjær', 'Male', 1997, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Rebecca Friis', 'Female', 1999, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Patrick Clausen', 'Male', 1998, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Kathrine Olesen', 'Female', 2001, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Rene Christiansen', 'Male', 1995, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Line Würtz', 'Female', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Stefan Møller', 'Male', 2003, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Mette Due', 'Female', 1997, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Jon Frederiksen', 'Male', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Sara Bech', 'Female', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Kim Andreasen', 'Male', 1996, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Anne Winther', 'Female', 1998, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Kenneth Schou', 'Male', 1999, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Lene Krogh', 'Female', 2004, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Thomas Bjerre', 'Male', 1995, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Julie Munch', 'Female', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Rasmus Hvid', 'Male', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Laura Damgaard', 'Female', 1999, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Anders Ryberg', 'Male', 1998, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Marie Sand', 'Female', 2003, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Morten Kragh', 'Male', 1997, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Nadia Brandt', 'Female', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Filip Jeppesen', 'Male', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Tanja Bertelsen', 'Female', 1998, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Martin Toft', 'Male', 1994, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Sofia Lind', 'Female', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Oliver Hald', 'Male', 2003, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Camilla Skov', 'Female', 1999, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Emil Brun', 'Male', 1998, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Kristine Falk', 'Female', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Magnus Ravn', 'Male', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Helena Enevoldsen', 'Female', 1997, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Jakob Vad', 'Male', 1996, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Emma Brink', 'Female', 2004, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Victor Gade', 'Male', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Cecilie Buhl', 'Female', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Mark Mikkelsen', 'Male', 1999, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Mia Johansen', 'Female', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Kasper Nørgaard', 'Male', 1998, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Laura Aagaard', 'Female', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Emil Hartmann', 'Male', 1997, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Mathilde Sejersen', 'Female', 2003, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Oliver Birk', 'Male', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Sabrina Jessen', 'Female', 1999, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Andreas Kaas', 'Male', 1996, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Nina Lundgaard', 'Female', 2004, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Frederik Warming', 'Male', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Sofie Kruse', 'Female', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Mikkel Villumsen', 'Male', 1998, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Katrine Frost', 'Female', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Simon Madsborg', 'Male', 1997, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Louise Brandt', 'Female', 1999, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Rasmus Holck', 'Male', 2003, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Amalie Kjeldsen', 'Female', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Jakob Høyer', 'Male', 1994, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Camilla Vang', 'Female', 1998, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Benjamin Dahlgaard', 'Male', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Tina Lykke', 'Female', 2004, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Sebastian Vester', 'Male', 1997, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Mille Krohn', 'Female', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Victor Rosen', 'Male', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Julie Hassing', 'Female', 1998, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Christian Bülow', 'Male', 1995, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Emma Guldberg', 'Female', 2003, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Noah Eskildsen', 'Male', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Helene Brinch', 'Female', 1999, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Martin Refslund', 'Male', 1996, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Lærke Husted', 'Female', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Philip Hedegaard', 'Male', 1998, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Ditte Mølgård', 'Female', 2000, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Tobias Balle', 'Male', 2004, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Sanne Voss', 'Female', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Jonas Friisberg', 'Male', 1997, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Pia Brun Hansen', 'Female', 1999, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Morten Søby', 'Male', 1995, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Rebecca Falkenberg', 'Female', 2003, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Magnus Terkelsen', 'Male', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Anna-Maria Madsen', 'Female', 1998, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Oliver Bachmann', 'Male', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Freja Bjørn', 'Female', 2000, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Alexander Dueholm', 'Male', 1997, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Mette Stensgaard', 'Female', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Daniel Kragh Andersen', 'Male', 1999, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Josefine Norup', 'Female', 2004, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Lukas Bering', 'Male', 1996, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Clara Hjelm', 'Female', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Mark Feldborg', 'Male', 2000, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Sofie Ellegaard', 'Female', 2002, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Andreas Birkedal', 'Male', 1998, 1);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Freja Holmgaard', 'Female', 2001, 0);",
    "INSERT INTO students (name, gender, birth_year, has_former_degree) VALUES ('Mikkel Vinter', 'Male', 2000, 0);"
]

# Execute each insert-into command generated by AI with a for loop
for sql in sql_statements:
    cursor.execute(sql)

# Commit the changes
conn.commit()


# Opgave 3:
# Lav et script til at tømme tabellerne for data. Her bruges DELETE FROM kommandoen.

# Delete all data inside the students table without deleting the table itself
# cursor.execute('DELETE FROM students')

# Commit the changes
# conn.commit()

# Close the database
conn.close()