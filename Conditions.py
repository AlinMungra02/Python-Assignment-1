#1. Check whether a number is positive, negative, or zero.
print("---------------program 1-----------------")

num = int(input("Enter a number: "))

if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

#2. Check whether a person is eligible to vote.
    print("---------------program 2-----------------")

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#3. Find the largest of three numbers.
print("---------------program 3----------------")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b and a > c:
    print("Largest number =", a)
elif b > a and b > c:
    print("Largest number =", b)
else:
    print("Largest number =", c)
    
#4. Check whether a year is a leap year.
    print("---------------program 4-----------------")

year = int(input("Enter a year: "))

if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
    
#5. Create a grade system based on marks.
    print("---------------program 5-----------------")

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")
    
#6. Check whether a number is divisible by 5 and 11.
    print("---------------program 6-----------------")

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Number is divisible by 5 and 11")
else:
    print("Number is not divisible by 5 and 11")
    
#7. Create a simple calculator using if-elif-else.
    print("---------------program 7-----------------")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result =", a + b)
elif op == "-":
    print("Result =", a - b)
elif op == "*":
    print("Result =", a * b)
elif op == "/":
    print("Result =", a / b)
else:
    print("Invalid operator")    

