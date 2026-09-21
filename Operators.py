#1. Perform addition, subtraction, multiplication, and division.
print("---------------program 1-----------------")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)

#2. Find the remainder and quotient of two numbers.
print("---------------program 2-----------------")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

quotient = a // b
remainder = a % b

print("Quotient =", quotient)
print("Remainder =", remainder)

#3. Check whether a number is even or odd.
print("---------------program 3-----------------")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


#4. Compare two numbers using relational operators.
print("---------------program 4-----------------")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("a > b :", a > b)
print("a < b :", a < b)
print("a == b :", a == b)
print("a != b :", a != b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)


#5. Demonstrate logical operators (and, or, not).
print("---------------program 5-----------------")

a = True
b = False

print("AND :", a and b)
print("OR  :", a or b)
print("NOT :", not a)


#6. Demonstrate assignment operators (+=, -=, *=, /=).
print("---------------program 6-----------------")

a = 10

a += 5
print("After += :", a)

a -= 3
print("After -= :", a)

a *= 2
print("After *= :", a)

a /= 4
print("After /= :", a)


#7. Find the largest of two numbers using comparison operators.
print("---------------program 7-----------------")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest number =", a)
else:
    print("Largest number =", b)
