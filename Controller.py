#=============================================================================
# PROGRAMMER1: Samuel Muvdi
# PANTHER ID1: 6100199
# CLASS: COP5507
#
# PROGRAMMER2: Hanson Nguyen
# PANTHER ID2: 
# CLASS: COP5507
#
# SEMESTER: Spring 2023
# CLASSTIME: Online Course
#
# Project: Description of project
# DUE: Sunday, April 19, 2025
#
# CERTIFICATION: I certify that this work is my own and that
# none of it is the work of any other person.
#=============================================================================

import numpy as np
print("Enter (R)andom or (M)anual payoff enteries: ")
entry = input()
entry = entry.upper()

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of cols: "))

p1_strat = []
p2_strat = []

if entry == 'M':
    print("Add payoffs for player 1 by rows: ")
    p1_payoff = []
    p2_payoff = []
    pays = cols * rows
    
    for i in range(pays):
        p1_payoff.append(int(input()))
    p1_strat = np.array(p1_payoff).reshape(rows, cols)

    print("Add payoffs for player 2 by rows: ")
    for i in range(pays):
        p2_payoff.append(int(input()))
    p2_strat = np.array(p2_payoff).reshape(rows, cols)

for i in range(rows):
    for j in range (cols):
        if j == cols - 1:
            print( "(" + str(p1_strat[i,j]) + "," + str(p2_strat[i,j]) + ")")
        else:
            print( "(" + str(p1_strat[i,j]) + "," + str(p2_strat[i,j]) + ")", end = " ")





