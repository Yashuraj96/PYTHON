
1. Write a function for arithmetic operators(+,-,*,/) 
 
def addition(a,b):
   c=a+b;
   return c
def subraction(a,b):
   c=a-b;
   return c
def multiplication(a,b):
   c=a*b;
   return c
def division(a,b):
   c=a/b;
   return c
v=float(input("Enter the first value "));
b=float(input("Enter the second value "));
add=addition(v,b)
print(add);
sub=subraction(v,b)
print(sub);
mul=multiplication(v,b)
print(mul);
div=division(v,b)
print(div);


2. Write a method for increment and decrement operators(++, --) 
 
i=float(input("Enter the initial Value for A "));
j=int(input("Enter 1 for increment 0 for decrement "));
k=int(input("Enter the Number of times the inc or dec needed "));
if j==1:
   while (k>0):
      i=i+1;
      k=k-1;
else:
   while (k>0):
      i=i-1;
      k=k-1;
print(i);


3. Write a program to find the two numbers equal or not.

i=int(input("Enter the First value "));
j=int(input("Enter the Second value "));
if i==j:
   print("The Values are Equal");
else:
   print("The values entered are not equal");


4. Program for relational operators (<,<==, >, >==) 
 
i=int(input("Enter the First value "));
j=int(input("Enter the Second value "));
if i==j:
   print("The Values are Equal");
if i>j:
   print("value One is greater");
if i<j:
   print("Value Two is Greater");
else:
   print("Nothing is possible");


5. Print the smaller and larger number

NumList = []
Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

smallest = largest = NumList[0]

for j in range(1, Number):
    if(smallest > NumList[j]):
        smallest = NumList[j]
        min_position = j

    if(largest < NumList[j]):
        largest = NumList[j]
        max_position = j

print("The Smallest Element in this List is : ", smallest)
print("The Largest Element in this List is : ", largest)
