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
import pandas as pd

print("Enter (R)andom or (M)anual payoff enteries: ")
entry = input()
entry = entry.upper()

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of cols: "))

while rows < 1 or rows > 9 and cols < 1 or cols > 9:
    print("\n!!! Please enter rows and columns of size 1 - 9 !!!\n")
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
        p1_payoff.append(str(input()))
    p1_strat = np.array(p1_payoff).reshape(rows, cols)

    print("Add payoffs for player 2 by rows: ")
    for i in range(pays):
        p2_payoff.append(str(input()))
    p2_strat = np.array(p2_payoff).reshape(rows, cols)

strategies_p1 = []
for i in range(rows):
    strategies_p1.append('A'+ str(i))

strategies_p2 = []
for i in range(cols):
    strategies_p2.append('B'+ str(i))

print("==="*pays)
print("Player: Player 1's Strategies")
print(strategies_p1)
print("==="*pays)
print("Player: Player 2's Strategies")
print(strategies_p2)
print("==="*pays)

print("\n")
print("Player 1's payoffs:\n", p1_payoff)
print("===" * pays)
print("player 2's payoffs:\n", p2_payoff)
print("===" * pays)
print("\n !!! DISPLAY NORMAL FORM !!!")


for i in range(rows):
    for j in range (cols):
        if j == cols - 1:
            print( "(" + str(p1_strat[i,j]) + "," + str(p2_strat[i,j]) + ")")
        else:
            print( "(" + str(p1_strat[i,j]) + "," + str(p2_strat[i,j]) + ")", end = " ")

print("===" * pays)
print("\n !!! Finding Nash EQ !!! \n")
print("===" * pays)

t_p1 = []
max_p1 = []
t_p1 = p1_strat.transpose(1, 0)
max_p1 = list(map(max,t_p1[::,::]))


max_p2 = []
max_p2 = list(map(max,p2_strat[::,::]))

print("Player 1's best strategies for Nash EQ:\n", max_p1)
print("===" * pays)
print("player 2's best strategies for Nash EQ:\n", max_p2)
print("===" * pays)


for i in range(len(p1_strat)):
    for k in range(len(max_p1)):
        p1_strat[p1_strat == max_p1[k]] = 'H'

for i in range(len(p2_strat)):
       for k in range(len(max_p2)):
        p2_strat[p2_strat == max_p2[k]] = 'H'

print("\n !!! Game Matrix with Nash EQ !!! \n")
print("===" * pays)
for i in range(rows):
    for j in range (cols):
        if j == cols - 1:
            print( "(" + str(p1_strat[i,j]) + "," + str(p2_strat[i,j]) + ")")
        else:
            print( "(" + str(p1_strat[i,j]) + "," + str(p2_strat[i,j]) + ")", end = " ")
print("===" * pays)