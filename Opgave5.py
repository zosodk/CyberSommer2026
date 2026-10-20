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

#import  sqlite3 and connection to the database
import sqlite3 as sql
conn = sql.connect("students.db")
cur = conn.cursor()

#the main program
while True:
    chosen = False
    retry = False

    #letting the user chose what they want to sort after
    choice= input("hi welcome to the sorting program"
          "\nhow would you like to sort the students pick one of these 2 options"
          "\n1 birth year"
          "\n2 if they have a former degree\n")

    #birth year sorting
    if choice == "1":

        #making sure something had been sorted
        while chosen == False:
            year_select=input("\nyou have choosen to sort them by birth year, write a year and all students born before that year will be printed\n")

            #checking if the year written is actual a valid year
            if year_select.isdigit() == True and int(year_select)>0:
                cur.execute("SELECT * FROM students WHERE birth_year < ?", (year_select,))
                data = cur.fetchall()

                #printing the students that are born before the chosen year
                if len(data) == 0:
                    print("there are no students born before that year")
                    chosen = True
                else:
                    for row in data:
                        print(f"student:{row[1]} was born at {row[3]}")
                    chosen = True

                #a function to let the user sort again if they want
                retrier = input("\nwould you like to sort again? yes or no\n")
                while retry == False:
                    if retrier.lower() == "yes" or retrier.lower() == "y":
                        retry = True
                    elif retrier.lower() == "no" or retrier.lower() == "n":
                        break
                    else:
                        print("\nthat was not a yes or a no\n")

            #telling the user if their input is not valid
            else:
                print("you did not type a valid birth year")

    #sorting by if they have a degree or not
    elif choice == "2":

        #making sure a sort happens
        while chosen == False:
            degree = input("\nyou have chosen to sort by if a student has a degree or not\n"
                           "write yes to see all students with a former degree"
                           "\nwrite no to see all students who doesnt have a former degree\n")

            #telling the program what it should do if they want to see the students without a former degree
            if degree.lower() == "no" or degree.lower() == "n":
                cur.execute("SELECT name FROM students WHERE has_former_degree = 0")
                data = cur.fetchall()

                #printing the data
                for row in data:
                    print(f"Student:{row[0]} doesnt have a former degree")

                #the function to let the user go back and sort again
                retrier = input("\nwould you like to sort again? yes or no\n")
                while retry == False:
                    if retrier.lower() == "yes" or retrier.lower() == "y":
                        retry = True
                    elif retrier.lower() == "no" or retrier.lower() == "n":
                        break
                    else:
                        print("\nthat was not a yes or a no\n")
                chosen = True

            # telling the program what it should do if they want to see the students with a former degree
            elif degree.lower() == "yes" or degree.lower() == "y":
                cur.execute("SELECT name FROM students WHERE has_former_degree = 1")
                data = cur.fetchall()

                #printing the data
                for row in data:
                    print(f"Student:{row[0]} has a former degree")

                #letting the user go back and sort again if they want to
                retrier = input("\nwould you like to sort again? yes or no\n")
                while retry == False:
                    if retrier.lower() == "yes" or retrier.lower() == "y":
                        retry = True
                    elif retrier.lower() == "no" or retrier.lower() == "n":
                        break
                    else:
                        print("\nthat was not a yes or a no\n")
                chosen = True

            #making sure they gave a valid input
            else:
                print("that was not a yes or no")

    #if something have been chosen to be sorted and the user wants to sort again then they can
    if chosen == True and retry == True:
        continue

    #if something have been chosen to be sorted and the user doesnt want to sort again
    elif chosen == True and retry == False:
        break

    #making sure they gave a valid input in the beginning
    else:
        print("that wasn't a valid input write 1 or 2\n")

#ending the program and closing the connection
print("thanks for using the sorting program have a nice day")
conn.close()