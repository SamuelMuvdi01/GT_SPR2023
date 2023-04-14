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





#Printing Player 1's payoffs
print("------------------------------------")
print("Player: Player1's strategies")
print("------------------------------------")
print("{", end = "")
for i in range(rows):
    if i == rows - 1:
        print("A" + str(i+1) + "}")
    else:
        print("A" + str(i+1) + ", ", end = "")

print("\n------------------------------------")
print("Player: Player1's payoffs")
print("------------------------------------")
flag = 0
for i in range(len(p1_payoff)):
    flag += 1
    if flag == cols: 
        print("%3s" % str(p1_payoff[i]))
        flag = 0
    else:
        print("%3s" % str(p1_payoff[i]) + ", ", end = "")





#Printing Player 2's payoffs

print("\n------------------------------------")
print("Player: Player2's strategies")
print("------------------------------------")
print("{", end = "")
for i in range(cols):
    if i == cols - 1: 
        print("B" + str(i+1) + "}")
    else:
        print("B" + str(i+1) + ", ", end = "")

print("\n------------------------------------")
print("Player: Player2's payoffs")
print("------------------------------------")
flag = 0
for i in range(len(p2_payoff)):
    flag += 1
    if flag == rows: 
        print("%3s" % str(p2_payoff[i]))
        flag = 0
    else:
        print("%3s" % str(p2_payoff[i]) + ", ", end = "")



print("\n=======================================")
print("Display Normal Form")
print("=======================================")

for i in range(cols):
    if i < cols - 1:
        print("            " + "B" + str(i + 1), end = "   ")
    else:
        print("            " + "B" + str(i + 1) + "     ")
dashes = 15 * cols + 5
print("   " + "-" * (dashes))

#+ "," + str(p2_strat[i,j]) + ")", end = "")
#+ "," + str(p2_strat[i,j]) + ")", end = "")
rightpayoff = ""
leftpayoff = ""
for i in range(rows):
    print("A" + str(i + 1) + " | ", end = "")
    for j in range (cols):
        if j == cols - 1:
            print("%4s" %  "(", end = "")
            print("%3s" % str(p1_strat[i,j]), end = "")
            rightpayoff =  str(p2_strat[i,j])
            print("," + "{:<3}".format(rightpayoff), end = "")
            print(")", end = "")
            print("%4s" % "|")
        else:
            print("%4s" %  "(", end ="")
            print("%3s" % str(p1_strat[i,j]) + ",", end = "")
            leftpayoff =  str(p2_strat[i,j])
            print("{:<3}".format(leftpayoff), end = "")
            print(")", end = "")
            print("%4s" % "|", end = "")
    print("   " + "-" * (dashes))









