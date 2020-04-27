#The code that imports data from a CSV spreadsheet

import sys
import csv
from cs50 import SQL

#Check, is ARGV == 2
if len(sys.argv) != 2:
    print("Usage: python import.py database.csv")
    sys.exit()

#Open csv file
db_file = []
try:
    with open (sys.argv[1]) as csv_file:
        file = csv.reader(csv_file)
        for line in file:
            db_file.append(line)

except FileNotFoundError:
    print("Wrong file or file path")
    sys.exit()

#Prepare file to be loaded into database
db_file = db_file[1:len(db_file)]
import_file = []
for line in db_file:
    names = line[0].split()
    if len(names) == 2:
        empty_middle = [names[0], None, names[1]]
        append_line = [empty_middle[0], empty_middle[1], empty_middle[2], line[1], line[2]]
        import_file.append(append_line)
    else:
        append_line = [names[0], names[1], names[2], line[1], line[2]]
        import_file.append(append_line)

#Connect "students" SQLite database
db = SQL("sqlite:///students.db")

#Write into database
for row in import_file:
    db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)", row[0], row[1], row[2], row[3], row[4])