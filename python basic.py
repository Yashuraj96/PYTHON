1. Write a program to print your name.
print("Yashodha R")


2. Write a program for a Single line comment and multi-line comments
# PROGRAM IN PYTHON
print("Above is the single line comment")

""" Program in python
    this is multiline comment
    ends here"""
print("Above is the multiline comment")


3. Define variables for different Data Types int, Boolean, char, float, double and print on the 
Console

f = int(12)

x = 'Yashodha R'
print(bool(x))

j = ("Yashodha R")
print(type(j))

f = (12.0)
print(type(f))


4. Define the local and Global variables with the same name and print both variables and 
understand the scope of the variables

def sample(a,b):
   c=a+b;
   return c
def sample1(a,b):
   c=a-b;
   return c

v=30;
b=20;
ans=sample(v,b)
print(ans);
ans1=sample1(v,b)
print(ans1);
