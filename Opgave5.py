# Et script til at filtrere data (lave en udvælgelse med SELECT). Det kunne f.eks. være alle students der
# bor i Esbjerg
#cursor.execute("""
#CREATE TABLE IF NOT EXISTS students (
#    id INTEGER PRIMARY KEY,
#    name TEXT,
#    gender TEXT,
#    birth_year INTEGER
#    has_former_degree INTEGER
#)
#""")

import sqlite3 as sql
conn = sql.connect("students.db")
cur = conn.cursor()

while True:
    chosen = False
    retry = False
    choice= input("hi welcome to the sorting program"
          "\nhow would you like to sort the students pick one of these 2 options"
          "\n1 birth year"
          "\n2 if they have a former degree\n")
    if choice == "1":
        while chosen == False:
            year_select=input("\nyou have choosen to sort them by birth year, write a year and all students born before that year will be printed\n")
            if year_select.isdigit() == True:
                cur.execute("SELECT * FROM students WHERE birth_year < ?", (year_select,))
                data = cur.fetchall()
                for row in data:
                    print(f"student:{row[1]} was born at {row[3]}")
                if len(data) == 0:
                    print("there are no students born before that year")
                chosen = True
                retrier = input("\nwould you like to sort again? yes or no\n")
                while retry == False:
                    if retrier.lower() == "yes" or retrier.lower() == "y":
                        retry = True
                    elif retrier.lower() == "no" or retrier.lower() == "n":
                        break
                    else:
                        print("\nthat was not a yes or a no\n")
            else:
                print("you did not type a valid birth year")

    elif choice == "2":
        while chosen == False:
            degree = input("\nyou have chosen to sort by if a student has a degree or not\n"
                           "write yes to see all students with a former degree"
                           "\nwrite no to see all students who doesnt have a former degree\n")
            if degree.lower() == "no" or degree.lower() == "n":
                cur.execute("SELECT name FROM students WHERE has_former_degree = 0")
                data = cur.fetchall()
                for row in data:
                    print(f"Student:{row[0]} doesnt have a former degree")
                retrier = input("\nwould you like to sort again? yes or no\n")
                while retry == False:
                    if retrier.lower() == "yes" or retrier.lower() == "y":
                        retry = True
                    elif retrier.lower() == "no" or retrier.lower() == "n":
                        break
                    else:
                        print("\nthat was not a yes or a no\n")
                chosen = True
            elif degree.lower() == "yes" or degree.lower() == "y":
                cur.execute("SELECT name FROM students WHERE has_former_degree = 1")
                data = cur.fetchall()
                for row in data:
                    print(f"Student:{row[0]} has a former degree")
                retrier = input("\nwould you like to sort again? yes or no\n")
                while retry == False:
                    if retrier.lower() == "yes" or retrier.lower() == "y":
                        retry = True
                    elif retrier.lower() == "no" or retrier.lower() == "n":
                        break
                    else:
                        print("\nthat was not a yes or a no\n")
                chosen = True
            else:
                print("that was not a yes or no")
    if chosen == True and retry == True:
        continue
    elif chosen == True and retry == False:
        break
    else:
        print("det er ikke et valid input kun vælg 1 eller 2\n")
conn.close()