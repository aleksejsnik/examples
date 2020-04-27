# Script that take a sequence of DNA
# and a CSV file containing STR counts for a list of individuals
# and then output to whom the DNA (most likely) belongs

import sys
import csv
from itertools import groupby
import re

def main():
    #Check, is ARGV == 3
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")

    #Create DNA database
    dna_db = get_db(sys.argv[1])

    #Create sequences list
    seq_string = get_sequences(sys.argv[2])

    #Create iterator list
    i_list = get_ilist(dna_db[0])

    #Create repeats list
    repeats_lst = cons_repeats(seq_string, i_list)

    #Lookup repeats list in DNA database
    result = lookup_dna_match(dna_db, repeats_lst)
    if result == None:
        print("No match")
    else:
        print(result)


# Create DNA database, import from database files
def get_db(file):
    db = []

    try:
        with open (file) as csv_file:
            db_file = csv.reader(csv_file)
            for line in db_file:
                db.append(line)
        return db

    except FileNotFoundError:
        print("Wrong database file or file path")
        sys.exit()



# Create sequences string
def get_sequences(seq_file):
    try:
        file = open(seq_file, "r")
        seq_list = file.readlines()
        file.close()
        seq = str(seq_list)
        return seq

    except FileNotFoundError:
        print("Wrong sequences file or file path")
        sys.exit()

# Create iterator list
def get_ilist(db_head):
    l = len(db_head)+1
    ilist = db_head[1:l]
    return ilist

# Compute the longest run of consecutive repeats of the STR 
# in the DNA sequence to identify.
def cons_repeats (seq_string, i_list):
    repeats = []
    for element in i_list:

        #Split sequence string by STR and create STR list
        str_list = re.split(rf"({element})", seq_string)

        #Clear str_list from empty strings
        clear_list = list(filter(None, str_list))

        #Group STRs by consecutive repeats and count repeats
        group_str_list = [[k, sum(1 for i in j)] for k, j in groupby(clear_list)]

        #Lookup bigget repeat by STR
        rep_counter = 0
        for pairs in group_str_list:
            if element == pairs[0]:
                if pairs[1] > rep_counter:
                    rep_counter = pairs[1]
        repeats.append(str(rep_counter))

    return repeats

# Lookup repeats list in DNA database
def lookup_dna_match(dna_db, repeats_lst):
    l = len(dna_db)
    m = len(dna_db[0])
    match_db = dna_db[1:l]
    for lst in match_db:
        if repeats_lst == lst[1:m]:
            return lst[0]

main()
