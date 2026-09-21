#5. Loops

#1. Print numbers from 1 to 10 using a for loop.


print("---------------program 1-----------------")

for i in range(1, 11):
    print(i)

#2. Print numbers from 10 to 1 using a while loop.

print("---------------program 2-----------------")

i = 10

while i >= 1:
    print(i)
    i -= 1

#3. Print the multiplication table of a number.

print("---------------program 3-----------------")

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

#4. Find the sum of numbers from 1 to n.

print("---------------program 4-----------------")


n = int(input("Enter n: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print("Sum =", sum)

#5. Find the factorial of a number.

print("---------------program 5-----------------")


n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)

#6. Print all even numbers between 1 and 100.

print("---------------program 6-----------------")


for i in range(2, 101, 2):
    print(i)

#7. Reverse a number using a loop.

print("---------------program 7-----------------")


n = int(input("Enter a number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse =", reverse)

#8. Count the digits of a number.

print("---------------program 8-----------------")


n = int(input("Enter a number: "))
count = 0

while n > 0:
    n = n // 10
    count += 1

print("Number of digits =", count)


#9. Check whether a number is prime.

print("---------------program 9-----------------")

n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")


#10. Print Fibonacci series up to n terms.
    
print("---------------program 10-----------------")


n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c
