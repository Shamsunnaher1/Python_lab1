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