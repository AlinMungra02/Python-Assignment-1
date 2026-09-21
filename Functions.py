# 1. Function to print "Hello, World!"

def hello():
    print("Hello, World!")

print("---------------program 1-----------------")
hello()
print("\n")


# 2. Function that takes a name and prints a greeting

def greeting(name):
    print("Hello", name)

name = "ALin"

print("---------------program 2-----------------")
greeting(name)
print("\n")


# 3. Function to add two numbers

def add(a, b):
    return a + b

num1 = 10
num2 = 20

print("---------------program 3-----------------")
print("Addition:", add(num1, num2))
print("\n")


# 4. Function to find the square of a number

def square(num):
    return num * num

num = 5

print("---------------program 4-----------------")
print("Square:", square(num))
print("\n")


# 5. Function to check whether a number is even or odd

def even_odd(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

num = 7

print("---------------program 5-----------------")
even_odd(num)
print("\n")


# 6. Function to find the maximum of two numbers

def maximum(a, b):
    if a > b:
        return a
    else:
        return b

num1 = 25
num2 = 15

print("---------------program 6-----------------")
print("Maximum:", maximum(num1, num2))
print("\n")


# 7. Function to convert Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = 25

print("---------------program 7-----------------")
print("Celsius:", celsius)
print("Fahrenheit:", celsius_to_fahrenheit(celsius))
print("\n")


# 8. Function to calculate the area of a circle

def area_of_circle(radius):
    return 3.14 * radius * radius

radius = 5

print("---------------program 8-----------------")
print("Radius:", radius)
print("Area of circle:", area_of_circle(radius))
print("\n")


# 9. Function to calculate the factorial of a number

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

num = 5

print("---------------program 9-----------------")
print("Factorial:", factorial(num))
print("\n")


# 10. Function to check whether a number is positive, negative, or zero

def check_number(num):
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")

num = -10

print("---------------program 10-----------------")
check_number(num)
print("\n")


# 11. Function to find the maximum of three numbers

def maximum_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

num1 = 10
num2 = 25
num3 = 15

print("---------------program 11-----------------")
print("Maximum:", maximum_three(num1, num2, num3))
print("\n")


# 12. Function to count vowels in a string

def count_vowels(text):
    count = 0
    for char in text:
        if char in "aeiouAEIOU":
            count = count + 1
    return count

text = "Hello World"

print("---------------program 12-----------------")
print("String:", text)
print("Number of vowels:", count_vowels(text))
print("\n")


# 13. Function to reverse a string

def reverse_string(text):
    return text[::-1]

text = "Alin"

print("---------------program 13-----------------")
print("Original string:", text)
print("Reverse string:", reverse_string(text))
print("\n")


# 14. Function to check whether a string is a palindrome

def palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

text = "madam"

print("---------------program 14-----------------")
print("String:", text)
print(palindrome(text))
print("\n")


# 15. Function to find the sum of all elements in a list

def list_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

numbers = [10, 20, 30, 40, 50]

print("---------------program 15-----------------")
print("List:", numbers)
print("Sum:", list_sum(numbers))
print("\n")


# 16. Function to find the largest element in a list

def largest(numbers):
    large = numbers[0]

    for num in numbers:
        if num > large:
            large = num

    return large

numbers = [10, 25, 15, 40, 30]

print("---------------program 16-----------------")
print("List:", numbers)
print("Largest element:", largest(numbers))
print("\n")


# 17. Function to remove duplicate elements from a list

def remove_duplicates(numbers):
    new_list = []

    for num in numbers:
        if num not in new_list:
            new_list.append(num)

    return new_list

numbers = [10, 20, 10, 30, 20, 40]

print("---------------program 17-----------------")
print("Original list:", numbers)
print("After removing duplicates:", remove_duplicates(numbers))
print("\n")


# 18. Function to count how many times an element appears in a list

def count_element(numbers, element):
    count = 0

    for num in numbers:
        if num == element:
            count = count + 1

    return count

numbers = [10, 20, 10, 30, 10, 40]
element = 10

print("---------------program 18-----------------")
print("List:", numbers)
print("Element:", element)
print("Count:", count_element(numbers, element))
print("\n")


# 19. Function to check whether a number is prime

def prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

num = 17

print("---------------program 19-----------------")

if prime(num):
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")

print("\n")


# 20. Function to return all prime numbers between two numbers

def prime_numbers(start, end):
    primes = []

    for num in range(start, end + 1):
        if num >= 2:
            is_prime = True

            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break

            if is_prime:
                primes.append(num)

    return primes

start = 10
end = 30

print("---------------program 20-----------------")
print("Prime numbers:", prime_numbers(start, end))
print("\n")


# 21. Function to calculate Fibonacci numbers

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = 10

print("---------------program 21-----------------")
print("Fibonacci numbers:")
fibonacci(n)
print("\n")


# 22. Function to find the second-largest number in a list

def second_largest(numbers):
    first = numbers[0]
    second = None

    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num != first and (second is None or num > second):
            second = num

    return second

numbers = [10, 25, 15, 40, 30]

print("---------------program 22-----------------")
print("List:", numbers)
print("Second largest:", second_largest(numbers))
print("\n")


# 23. Function to sort a list without using sort()

def sort_list(numbers):
    new_list = numbers.copy()

    for i in range(len(new_list)):
        for j in range(i + 1, len(new_list)):
            if new_list[i] > new_list[j]:
                new_list[i], new_list[j] = new_list[j], new_list[i]

    return new_list

numbers = [40, 10, 30, 20, 50]

print("---------------program 23-----------------")
print("Original list:", numbers)
print("Sorted list:", sort_list(numbers))
print("\n")


# 24. Function to merge two lists and remove duplicates

def merge_lists(list1, list2):
    new_list = []

    for num in list1:
        if num not in new_list:
            new_list.append(num)

    for num in list2:
        if num not in new_list:
            new_list.append(num)

    return new_list

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

print("---------------program 24-----------------")
print("List 1:", list1)
print("List 2:", list2)
print("Merged list:", merge_lists(list1, list2))
print("\n")
