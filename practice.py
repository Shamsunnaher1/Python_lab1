#Basic

#Write a program to print your name, department, and university.
print("Shamsunnaher,CSE,Green University of Bangladesh")

#Write a program that takes two integers as input and prints their sum.
a = input("Enter 1st number:")
b = input("Enter another number:")
sum = int(a) + int(b)
print("Sum:", int(sum))

#Write a program that converts temperature from Celsius to Fahrenheit
c = input("Enter celcius temperature:")
f = float((int(c) * (9/5)) + 32 )
print("fahrenhite temperature is", float(f))

#Write a program to calculate area and perimeter of rectangle, circle, and triangle.
#Rectangle
l = input("Give the Length of a rectangle :")
w = input("Give the width of a rectangle :")
area = int(l) * int(w)
perimeter = 2 * (int(l) + int(w))
print("area of the rectangle is:", int(area))
print("perimeter of the rectangle is:", int(perimeter))

#Circle
r = input("Give the radius of a circle :")
carea = 3.1416 * (int(r) * int(r))
cperimeter = 2 * 3.1416 * int(r)
print("Area of the circle is : ", float(carea))
print("perimeter of the circle is:", float(cperimeter))

#triangle
a = input("Enter a side: ")
b = input("enter base: ")
c = input("enter another side: ")
h = input("enter height: ")
tarea = 0.5 * int(b) * int(h)
tperimeter = int(a) + int(b) + int(c)
print("Area of a triangle is: ", float(tarea))
print("Perimeter of a triangle is: ", int(tperimeter))

#Write a program to compute simple interest and compound interest.
P = input("enter principle: ")
R = input("enter the rate: ")
T = input("enter the time: ")
r = input("enter the anual interest rate: ")
n = input("enter the number of times interest is compounded per year: ")
t = input("enter the years: ")
SI = (int(P) * int(R) * int(T))/100
CI = (int(P) * (1 + (float(r)/float(n))) ** (int(n) * int(t)) ) - int(P)
print("Simple interest is: ", float(SI))
print("Compound interrest is: ", float(CI))

#Write a program to find the ASCII value of a character.
ch = input("enter a charescter: ")
AS = ord(ch)
print("The ASCII value is: ", int(AS))


#Write a program to swap two numbers using a temporary variable
a = 10
b = 20
temp = int(a)
a = int(b)
b = int(temp)
print(int(a), int(b))

#Write a program to swap two numbers without using a temporary variable
a = 10
b = 20
sum = a + b
a = sum - a
b = sum - b
print(int(a), int(b))


#Operators

#Write a program to check whether a number is even or odd using both modulo and bitwise operators
#Modulo
a = input("enter a number:")
if int(a) % 2 == 0:
    print("number is even")
else:
    print("number is odd")
    

#bitwise
if int(a) & 1 == 0:
    print("number is even")
else:
    print("number is odd")


#Write a program to find the maximum of three numbers using logical operators.
a = 12
b = 60
c = 9
if a > b and a > c:
    print("a is maximum")
elif b > a and b > c:
    print("b is maximum")
elif c > a and c > b:
    print("c is maximum")


#Write a program to convert total days into years, weeks, and remaining days.
days = input("enter total days: ")
years = int(days) / 365
r = int(days) % 365
weeks = int(r) / 7
rd = int(r) % 7
print("years: ", int(years), "weeks: ", int(weeks), "remaining days: ", int(rd)) 


#Write a program to find the minimum of two numbers using the conditional (ternary) operator.
a = 5
b = 10
if  a < b:
    print("a is minnimum")
else:
    print("b is minnimum")


#Write a program to demonstrate the behavior of pre-increment and post-increment operators.
a = 10
# pre increment
a = a + 2
b = a
print("pre increment value b: ", int(b))
print("pre increment value a: ", int(a))

a = 10
#post increment
b = a
a = a + 2
print("post increment value b: ", int(b))
print("post increment value a: ", int(a))


#Decision Making

#Write a program to check whether a number is positive, negative, or neutral.
a = input("enter a number: ")
if int(a) > 0:
     print("number is positive")
elif int(a) < 0:
     print("number is negative")
else:
     print("number is neutral")


#Write a program to check whether a given year is a leap year or not.
year = input("enter the year: ")
if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
    print("year is leap year")
else:
    print("not leap year")


#Write a program to find the grade of a student based on marks.
marks = input("enter marks: ")
if int(marks) >= 80:
    print("A+")
elif int(marks) >= 70 and int(marks) < 80:
    print("A")
elif int(marks) >= 60 and int(marks) < 70:
    print("A-")
elif int(marks) >= 50 and int(marks) < 60:
    print("B") 
elif int(marks) >= 40 and int(marks) < 50:
    print("C")
else:
    print("fail")


#Write a program to create a simple calculator using switch–case statements.
a = input("enter 1st number: ")
b = input("enter 2nd number: ")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = input("\nEnter your choice : ")

match choice:
    case '1':
        result = int(a) + int(b)
        print("Result: ", result )
    case '2':
        result = int(a) - int(b)
        print(" Result: ",result  )
    case '3':
        result = int(a) * int(b)
        print("Result: ", result  )
    case '4':
         result = int(a) / int(b)
         print("Result: ", result )
   


#Write a program to use goto to repeatedly take input from the user until 0 is entered.
while True:
    a = int(input("enter the number: "))   
    if a == 0:
        print("terminated.")
        break
    else:
        print("you enterd: ", int(a)) 


#Loops
#Write a program to print numbers from 1 to 100 using all three loops (for, while, and do–while).
for i in range(1, 101):
    print(i)
    
i = 1
while i < 101:
   print(i)
   i += 1


#Write a program to find the sum of the first N natural numbers.
N = int(input("enter the value of N: "))
i = 0
sum = 0
while i < N:
    sum += i 
    i += 1
print("sum", int(sum))
        

#Write a program to calculate the factorial of a given number.
N = int(input("enter the value of N: "))
i = 1
fact = 1
while i < N:
    fact *= i 
    i += 1
print("factorial", int(fact))


#Write a program to reverse a given number.
num = 123
rev = 0
while num != 0:
    n = int(num) % 10
    rev = (int(rev) * 10) + n
    num = int(num) // 10

print("reverse is: ", rev)


#Write a program to count the number of digits and find the sum of digits in a given number.
num = 1234
sum = 0
count = 0
while num != 0:
    n = int(num) % 10
    sum = int(sum) + n
    count += 1
    num = int(num) // 10

print("sum is: ", sum, "count is: ", count)  


#Write a program to generate and display the multiplication table of any given number.
N = input("enter the number: ")
print("multiplication table of: ", N)

for i in range(1,11):
    r = int(N) * i
    print(int(N), "*", i, "=", int(r) )


#Write a program to print all even numbers between two given limits
for i in range(1,50):
    if i % 2 == 0:
        print("even: ", i)


#Write a program to check whether a given number is a Prime number.
N = input("enter the number: ")
for i in range(2,int(N ** 0.5)+1):
    if N % i == 0:
    
