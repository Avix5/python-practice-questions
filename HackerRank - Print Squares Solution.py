"""
Problem: Print Squares

Description:
Given an integer n, print the square of all non-negative integers
less than n.

Input:
An integer n

Output:
Print the square of each number from 0 to n-1 on a separate line.

Example:
Input:
5

Output:
0
1
4
9
16
"""

# Taking input from user
n = int(input("Enter a number: "))

# Loop from 0 to n-1
for i in range(n):
    print(i * i)
