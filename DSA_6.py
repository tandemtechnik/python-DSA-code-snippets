# # Function to shuffle an array of size 2n
# def shuffleArray(a, n):
#     i, q, k = 0, 1, n
#     while(i < n):
#         j = k
#         while(j > i + q):
#             a[j - 1], a[j] = a[j], a[j - 1]
#             j -= 1
#         i += 1
#         k += 1
#         q += 1
#
# a = [1, 3, 5, 7, 2, 4, 6, 8]
# n = len(a)
# shuffleArray(a, int(n / 2))
# for i in range(0, n):
#     print(a[i], end = " ")

# # ***************************************************************
# GENERATE EVEN NUMBERS
# def generate_even_numbers(limit):
#   num = 0
#   while num <= limit:
#     yield num
#     num += 2

# evens = generate_even_numbers(11)
# print(evens)
# for num in evens:
#   print(num)

#********************************************************************
#GENERATE PRIME NUMBERS

# def generate_primes():
#   primes = []
#   num = 2
#   while True:
#     if all(num % prime != 0 for prime in primes):
#       yield num
#       primes.append(num)
#     num += 1

# prime_generator = generate_primes()
# primes = [next(prime_generator) for i in range(6)]
# print(primes)
# ***********************************************************************

# print([x for x in range(10) if x % 2 == 0])
# print([x for x in range(10) if x % 2])
# print([x for x in range(10) if x % 2 == 1])
# # ********************************************************************
#
# number = 10
# def func(number = 0):
#     number += 90
#     return number
# number = 20
# print(number, func(), func(40))
# ************************************************************************

# my_list = [1, 2, 3, 4, 5, 6]
# reduced_list = my_list[::2]
# reduced_list[1] = 10
# print(reduced_list)
# ******************************************************

# word = ("Banane")
# word.replace("e", "a")
# print(word)
# *****************************************************
#
# x = [1, 2, 3]
# y = x
# x.append(4)
# y = x + [5]
# print(y, x)
#
# import time
# for bdcount in range(10, 0, -1):
#     time.sleep(2)
#     print(bdcount)
# print()
# print("Happy Birthday Sophia!")
# print()
# print("May you soar above all the stars in Jesus name, A M E N.")
# num = [1, 2, 3, 4, 5]
# for i in num:
#     if i%2 == 0:
#         continue
#     print(i**2, end=' ')

# fruits = ["grapes", "bananas", "apples", "limes"]
# fruits.insert(3, "sour sop")
# print(len(fruits))

# counter = 0
# while counter < 10:
#     print("Great guy")
#     counter += 1

# import random
#
# for x in range(3):
#     print(random.randint(1,6))

# try:
#     a = 20
#     b = 0
#     print(a/b)
# except ZeroDivisionError:
#     print("Can't divide by zero")
# finally:
#     print("This code will execute anyway")

# my_dict = {
#     1: "One",
#     2: "Two",
#     3: "Three"
# }
# for x, y in my_dict.items():
#     print(x, "=", y)
#
# print(my_dict.get(5, "Value not present")


# def generate_even_numbers(limit):
#   num = 0
#   while num <= limit:
#     yield num
#     num += 2

# evens = generate_even_numbers(11)
# print(evens)
# for num in evens:
#   print(num)


# def generate_primes():
#   primes = []
#   num = 2
#   while True:
#     if all(num % prime != 0 for prime in primes):
#       yield num
#       primes.append(num)
#     num += 1

# prime_generator = generate_primes()
# primes = [next(prime_generator) for i in range(6)]
# print(primes)

# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide by zero")
#         return func(a, b)
#     return inner
#
# a=12
# b=4
# @smart_divide
# # result = def divide(12, 3):
# result = def divide(a, b):
#     # print(result)


# def fibonacci (n):
#   #creating an array in the function to find the nth number in fibonacci series. [0,1,1,...]
#    FibArray = [0] * (n+1)
#    FibArray[1] = 1
#    #Over here, we are adding elements of the series to the array using addition of provious 2 elements.
#    for i in range (2,n+1):
#       FibArray[i] = FibArray[i-1] + FibArray[i-2]
#    return FibArray[n]
# if __name__ == "__main__":
#    print(fibonacci (15))

# def fibonacci_of(n):
#     if n in {0, 1}:  # Base case
#         return n
#     return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case
# print(fibonacci_of(15))
# [(fibonacci_of(n) for n in range(15)]
# # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]


# Fibonacci numbers recursively in Python using recursive features. Here’s a Python code to calculate
# the nth Fibonacci number by using recursion:

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci (n-2)
# #import csv
# fib = fibonacci(15)
# print(fib)

# Frequently Asked Questions
# Q1. What is the Fibonacci series?
# A. The Fibonacci series is a sequence of numbers that starts with 0 and 1, in which every next
# number is the sum of the two previous ones
#
# Q2. What is the formula of the Fibonacci Series?
# A.  F(n) = F(n-1) + F(n-2)
#
# Q3. What is the Fibonacci series of 5?
# A. The Fibonacci series up to the 5th number is: 0, 1, 1, 2, 3. So, the Fibonacci number is 3.
#
# Q4. What are the first 20 Fibonacci series
# A. The first 20 Fibonacci series are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, and 4181.

# def is_positive(word):
#     words = (
#         'yes',
#         'correct',
#         'affirmative'
#         'agreed',
#     )
#     return word in words

# wd = is_positive(word)

# is_positive('agreed')

# dict1 = {
# "3": "love",
# "6": "computers",
# "2": "dogs",
# "4": "cats",
# "1": "I",
# "5": "you"
# }