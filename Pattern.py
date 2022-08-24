'''
PROBLEM:To print five *'s in the same line five times
Using nested for loops 
outer loop if for setting rows
inner loops are for columns
Using end parameter with print,we can print contents in a single line in loop
'''


def Stars_5(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


def Hash_5(n):
    for i in range(n):
        for j in range(n):
            print("#", end=" ")
        print()


'''
PROBLEM:To print stars in an increasing format for given numbers
Using nested for loops
In inner loop i increases in every iteration
'''


def Increasing_Star(n):
    for i in range(n):
        for j in range(i+1):  # i increases in every iteration from 0 to 4
            print("*", end=" ")
        print()


'''
PROBLEM:To print stars in an decreasing format for given numbers
Using nested for loops
In inner loop i is set to (i,n)
It refers as i increases in every iteration 
The values from i to n decreases
'''


def Decreasing_Star(n):
    for i in range(n):
        for j in range(i, n):  # HERE (i,n) refers starting condition
            print("*", end=' ')
        print()


'''
PROBLEM:To print stars in an Leftside Triangle format for given numbers
Using nested for loops
The first nested loop prints empty spaces of decreasing stars
The second nested loop prints stars of increasing stars
'''


def LeftSided_Tri(n):
    for i in range(n):
        for j in range(i, n):
            print(" ", end=" ")

        for j in range(i+1):
            print("*", end=" ")
        print()


'''
PROBLEM:To print stars in an Leftside Triangle format for given numbers
Using nested for loops
The first nested loop prints empty spaces of increasing stars
The second nested loop prints stars of decreasing stars
'''


def RightSided_Tri(n):
    for i in range(n):
        for j in range(i+1):
            print(" ", end=" ")

        for j in range(i, n):
            print("*", end=" ")
        print()


'''
PROBLEM:To print stars in a Mountain like format for given numbers
Using nested for loops
First Print Right_side_Triangle with a range of i instead of i+1
Second Print Left Sided_Triangle
'''


def Mountain(n):
    for i in range(n):
        for j in range(i, n):
            print(" ", end=' ')

        for j in range(i):
            print("*", end=" ")

        for j in range(i+1):
            print("*", end=" ")

        print()


def Reverse_Mountain(n):
    for i in range(n):
        for j in range(i+1):
            print(" ", end=" ")
        for j in range(i, n):
            print("*", end=" ")
        for j in range(i+1, n):
            print("*", end=" ")
        print()


# Stars_5(5)
# Hash_5(6)
# Increasing_Star(10)
# Decreasing_Star(10)
# LeftSided_Tri(5)
# RightSided_Tri(5)
# Mountain(10)
# Reverse_Mountain(10)
