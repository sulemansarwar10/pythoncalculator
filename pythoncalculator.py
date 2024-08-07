#Roll#  PIAIC59391
# Objective
# In this assignment, you will write a Python program to perform basic calculator operations: addition,
# subtraction, multiplication, and division.

# Instructions

# 1. Input and Operations
# - Option 1: User Input
# If you are familiar with taking user input in Python, write a program that takes two numbers and an
# operation (addition, subtraction, multiplication, or division) as input from the user and performs the
# corresponding operation.

a = input("Enter first number:")
b = input("Enter second number:")
c = input("Enter operation (+, -, *, /)")
if(c=='+'):
    print("Output is: ",int(a)+int(b))
elif(c=='-'):
    print("Output is: ",int(a)-int(b))
elif(c=='*'):
    print("Output is: ",int(a)*int(b))
elif(c=='/'):
    print("Output is: ",int(a)/int(b))
else:
    print("Invalid operator ")
