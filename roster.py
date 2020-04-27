# Script that prints a list of students 
# for a given house in alphabetical order

from cs50 import SQL
import sys

#Check, is ARGV == 2
if len(sys.argv) != 2:
    print("Usage: python roster.py house_name")
    sys.exit()

#Connect students SQLite database
db = SQL("sqlite:///students.db")

#SQL query
roster = db.execute("SELECT * FROM students WHERE house=? ORDER BY last, first", sys.argv[1])

#Print out executed query
for line in roster:
    first = line["first"]
    middle = line["middle"]
    last = line["last"]
    birth = line["birth"]
    if middle == None:
        print(f"{first} {last}, born {birth}")
    else:
        print(f"{first} {middle} {last}, born {birth}")


