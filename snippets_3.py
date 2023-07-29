# OPEN A FILE TO READ AND CLOSE IT
# with open('gfg.txt', 'r') as f:
#     file = f.read()
#     print(file)
# =====================================
# OPEN A FILE TO APPEND CONTENT AND CLOSE IT
# temp = None
# while True:
#     temp = input("Please enter your information!! ")
#     try:
#         with open('gfg.txt', 'a') as f:
#             f.write(temp)
#     except Exception as e:
#         print("There is a Problem", str(e))
# ===========================================================================

#  VARIABLES AND TEXT FORMATTING
# age = 58
# age += 2
# name = "Aniedi Abasi"
# print(f"My name is {name}, and my age is {age}")
# print("My name is " + str(name) + ", and my age is " + str(age))
# ==============================================================================

# # REGULAR EXPRESSION EXTRACTING URL
# import re
# def find(URL):
#   url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',URL)
#   return url
# # URL ='I am a blogger at https://170.187.134.184'
# URL ='I am a blogger at https://www.tandem.ng.com'
# print("searched url: ", find(URL))
# ================================================================================

# LOGICAL OPERATORS
# temp = int(input("What's the temperature outside today?:"))
# if temp > 10 and temp < 30:
#     print("Go outside and catch cruise")
# elif temp < 0 or temp > 30:
#     print("Better stay indoors, it's ugly outside")
# ==================================
# temp = 32
# if temp <= 0 or temp >= 30:
#     print("Temperature is bad")
# else:
#     print("Temperature is good")
# ==================================================================================

# WHILE LOOP F0R PERSISTENCE-INFINITE LOOPS
# name = ""
# while len(name) == 0:
#     name = input("Please enter your name>> ")
# print("Hello "+name)
# ===========================
# name = None
# while not name:
#     name = input("Please enter your name>> ")
# print("Hello "+name)
# ======================================================================

# TIMERS IN CODE EXECUTION
# import time
# for i in range(10,0,-1):
#     print("1")
#     time.sleep(1)
# print("Happy New Year!!!")
# ===================================================

# PASS, BREAK, CONTINUE IMPLEMENTATIONS
# phone = "123-456-7890"
# for i in phone:
#     if i == "-":
#         pass # break
#     else:
#         print(i, end="")
# ==============================
# phone = "123-456-7890"
# for i in phone:
#     if i == "-":
#         continue
#     print(i, end="")
# =======================================================

# NESTED LOOPS: The inner loop will complete its iteration before finishing one outer loop iteration
# cols = 3
# rows = 4
# sym = '*'
# for i in range(rows):
#     for j in range(cols):
#         print(i, j, end=' ')
#     #     print(sym, end='')
#     print()
# =================================
# num_pad = ((1, 2, 3,),
#            (4, 5, 6,),
#            (7, 8, 9,),
#            ("*", 0, "#"))
# for rows in num_pad:
#     # print(rows)
#     for nums in rows:
#         # print(nums) # remove the commas and parenthesis
#         print(nums, end=' ')
#     print() # prints in desired row, column format
# ====================================================================

# LIST []: Used to store multiple items in single variable

# TUPLE (): Collection which is ordered and unchangeable or immutable used to group related data together

# SET {}: collection which is unordered, unindexed, no duplicate values.

# DICTIONARY {}: A collection which is unordered and changeable, with unique key:value pairs.
#             Fast because they use hashing, allow us to access a value quickly.
# ===================================================================================

# FUNCTIONS: A block of code which is executed only when it is invoked. Helps maintain the DRY principle
# def hello(name):
#     # print("Hi "+name)
#     print(f"Hello {name},")
#     print("have a wonderful day!")
# hello("Tboy")
# hello("Grandma")
# ===================================================
# def hello(first_name, last_name, age): # add parameters (P = Place holders)
#     print("Hi "+first_name+ " " +last_name)
#     print("You are "+str(age)+ " years old") # ensures int is a str
#     print("Pls have a wonderful day!")
# parse matching number of positional arguments. (A = Actual values)
# hello("Tboy", "Andino", 10)
# hello("Grandma", "Ene", 65)
# ===============================================================
# *args is a parameter that will pack all arguments into a tuple.
# Enables a function to accept a varying amount of arguments
# ADD
# def add(*args):
#     sum_ = 0
#     args = list(args)
#     args[0] = 5
#     print(args)
#     for x in args:
#         sum_ += x
#     return sum_
# result = add(1, 2, 4, 6, 9)
# print(f"Result: {result}")
# ==============================================================================

# # RANDOMS
# import random
# x = random.randint(1, 6)
# print(x)
# y = random.random()
# print(y)
# ==========================================
# mylist = ['rock', 'paper', 'scissors']
# z = random.choice(mylist)
# print(z)
# =============================================
# cards = [1,2,3,4,5,6,7,8,9,"Q","K","J","A"]
# random.shuffle(cards)
# print(cards)
# ============================================
# import random
# class Dice:
#     def roll_dice(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return (first, second)
# dice = Dice()
# print(dice.roll_dice())
# ===========================================================================
# # GET INPUT FROM USER
# # # Get a list as input from user
# lst = []
# # ele = ""
# # number of elements as input
# n = int(input("Enter number of elements : "))
# # iterating till the range
# for i in range(0, n):
#     ele = input("Enter items: ")
#     lst.append(ele)# adding the element
# print(f"The list of items are: {lst}")
# ==================================================================

# # FUNCTION, MANIPULATING LIST OF STRINGS
# def name_adder(list):
#     i = 0
#     new_list = []
#     while i < len(list):
#         if list[i] != "": # Stop adding when "" is encountered
#             new_list.append(list[i])
#         else:
#             break
#         i = i+1
#     return new_list
# lst1=["Joe", "Sarah", "Mike", "Jess", "Matt", "", "Greg"]
# print(name_adder(lst1))
# =========================================================================

# WALRUS OPERATOR:
# print(happy := True)
# =====================================
# foods = []
# while food := input("What food do you like?") != 'quit':
#     foods.append(food)
# ======================================
# food = input("Enter a food you like (or q to quit): ")
# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter a food you like (or q to quit): ")
# print("Byee...")
# ========================================================================

# LAMBDA: has only one expression but accepts any number of arguments
# lambda parameters:expression
# double = lambda x: x*2
# multiply = lambda x, y: x * y
# add = lambda x, y, z, a: x + y + z + a
# print(multiply(2, 4))
# print(double(9))
# print(add(2, 1, 3, 5,))
# ======================================
# REDUCE
# import functools
# factorial = [5,4,3,2,1]
# result = functools.reduce(lambda x, y,:x * y, factorial)
# print(result)
# ==================
# letters = ["H", "E", "L", "L", "O"]
# word = functools.reduce(lambda x, y,: x + y, letters)
# print(word)
# ======================================
# MULTIPLICATION BY BRUTE FORCE & LIST COMPREHENSION
# mylist = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# squares = []
# for i in mylist:
#     squares.append(i*2)
# print(squares)

# squares = [i*2 for i in mylist]
# print(squares)
# *******************************************************
# my_list = [3, 1, 6, 2]
# my_list = sorted(my_list)
# print(my_list)
# # ================================================================

# COMPREHENSIONS
# # LIST COMPREHENSIONS
# For list of integers
# lst1 = []
# lst1 = [int(item) for item in input("Enter the list items : ").split()]
# print(lst1)
# =================================
# For list of strings
# lst2 = []
# lst2 = [item.capitalize() for item in input("Enter the list items : ").split()]
# print(lst2)
# ==================================
# import functools
# factorial = range(1, 6)
# for i in factorial:
#     squares = []
#     result = functools.reduce(lambda x, y: x + y, factorial)
#     squares.append(result)
# print(squares)

# squares = []
# for i in range(1, 11):
#     squares.append(i * i)
# print(squares)
# ========================================
# LIST COMPREHENSION:
# List = [expression for item in iterable]
# squares = [i * i for i in range(1, 11)]
# print(squares)

# student_scores = [100,90,80,70,60,50,40,30,20,0]
# passed_students = list(filter(lambda x: x >= 60, student_scores))
# print(passed_students)
#
# # List = [expression for item in iterable if conditional]
# passed_students = [x for x in student_scores if x >= 60]
# print(passed_students)
#
# # List = [expression (if/else conditional) for item in iterable]
# passed_students = [x if x >= 60 else "FAILED" for x in student_scores]
# print(passed_students)

# DICTIONARY  COMPREHENSION
# {key: expression for (key, value) in iterable}

# mydict = {x: x**2 for x in (2, 4, 6)}
# print(mydict)
# =============================================================

# FILE OBJECT
import os
# with open('aman.txt') as f: # Default is r for read
#     my_file = f.read()
# print(my_file)

# with open('test.txt', 'w') as file:
#     file.write(text)

# text = "This is some awesome testing text"
# text1 = "This is another awesome testing text "
# with open('gfg.txt', 'a') as file:
#     file.write("\n" + text)
#     file.write("\n" + text1)
# *************************************************************
# number = 10
# lots_of_numbers = [number for x in range(5, 100, 2) if (number := x)]
# print(number)
# for i in lots_of_numbers:
#     print(i)
# 99, the last value in the iterable elements

# mylist = list(range(1, 7))
# mylist.append(8)
# print(mylist)
# ========================================================================

# CLASSES
# class MyClass:
#     def __init__(self, num):
#         self.num = num
#
#     def instance_method(self):
#         self.num = 40
#         return f"{self.num}"
# obj = MyClass(5)
# # obj.instance_method()
# print(obj.num)
# ==================================================

# #SUM OF ALL NUMBERS IN A LIST
# prices = [12, 25, 18, 41]
# total = 0
# for price in prices:
#     total += price
# print(f"Total cost: ${total}")
# **********************************************
# #SUM OF ALL NUMBERS TILL n
# n = int(input("Please enter any positive number: "))
# if n < 0:
#     print("Error: Number must be positive")
# else:
#     sum = 0
#     for i in range(n + 1):
#         sum += i
#
#     # i = n
#     # while i > 0:
#     #     sum += i
#     #     i -= 1
# print(f"Sum of all positive numbers till {i} is {sum}")
# ======================================================================

# #Mapping digits to words
# digits = None
# while not digits:
#     digits = input("Enter Digits: ")
#     digits_mapping = {
#         '0': 'Zero',
#         '1': 'One',
#         '2': 'Two',
#         '3': 'Three',
#         '4': 'Four',
#         '5': 'Five',
#         '6': 'Six',
#         '7': 'Seven',
#         '8': 'Eight',
#         '9': 'Nine',
#     }
#     output = ''
#     for nums in digits:
#         output += digits_mapping.get(nums, "!") + " "
#     print(output)
# =========================================================================

# # Maximum Number with function
# numbers = [2, 1, 5, 0, 6, 34]
# def find_max(numbers):
#     maximum = numbers[0]
#     for number in numbers:
#         if number > maximum:
#             maximum = number
#     return maximum
# result = find_max(numbers)
# print(result)
#======================================================
# # Find minimum number function
# numbers = [12, 11, 5, 87, 6, 34]
# def find_min(numbers):
#     minimum = numbers[0]
#     for number in numbers:
#         if minimum > number:
#             minimum = number
#     return minimum
# result = find_min(numbers)
# print(result)
# ==================================================================
# # Shallow copy:
# original_list = [1, 2, 3, [4, 5]]
# shallow_copy = original_list.copy()
# original_list[3].append(6)
# print(original_list)
# print(shallow_copy)
# ===========================================
# # Deep Copy:
# import copy
# original_list = [1, 2, 3, [4, 5]]
# deep_copy = copy.deepcopy(original_list)
# original_list[3].append(6)
# print(original_list)
# print(deep_copy)
#===========================================================================

# # Coding Challenge
# for i in range(3):
#     for j in range(3):
#         print(i*j, end=' ')
#     print()
# # 000012024
#============================================================================

# # Count number of words that contain letter "s"
# my_str = "Oranges and lemons, Say the bells of St. Clement's. " \
#         "You owe me three farthings, Say the bells of St. Martin's"
# def count_l(str):
#     c = 0
#     for i in str.split():
#         if "s" in i.lower():
#             c = c + 1
#         else:
#             pass
#     return c
# print(count_l(my_str))
#=============================================================================================

# JOIN METHOD
# # JOIN method of string with tuples: Join the tuple's elements to get a proper email address.
# addresses=("Mr.Hathaway", "amymail.com")
# email = "@".join(addresses)
# print(email)
# ================================================
# # JOIN METHOD Changing list of strings into a string
# list_of_strings = ['My', 'name', 'is', 'Tandem']
# print(' '.join(list_of_strings))
# ==================================================================================

# POP METHOD
# popleft() permanently removes from list left side entry.
# from collections import deque
# def names_list():
#     names = deque(['John', 'Oscar', 'Faith'])
#     names.append('Eric')
#     names.append('David')
#     names.popleft()
#     names = set(names)
#     names.pop()
#     return names
# print(names_list())
# ============================================================================

# # SPLIT Method
# str="101:102:103:201:202"
# lst = str.split(":")
# print(lst)

# # Rstrip method to remove from the right side only
# str="@Bloomberg@@@@@###"
# str = str.rstrip("@#")
# print(str)

# # Using a combination of .split() and .lstrip() methods, get the word "Derivatives".
# str="......Macroeconomics,...........Derivatives"
# lst = str.split(",")
# ans_1 = lst[1].lstrip(".")
# print(ans_1)

# # Format method to fill multiple values
# str = "{}, {}, {}".format(1, 2, 3)
# print(str)
# =========================================================================

# NESTED Data, ACCESSING DICTIONARY VALUES
# What color is violet
# nested_lst = [{"orange": "orange"}, {"rose": "red"}, {"violet": "blue"}]
# ans_1 = nested_lst[2]["violet"]
# print(ans_1)

# # Print the value of the roads key from the nested dictionary
# nested_dict = {"Dakar":{"weather":"sunny", "roads":"dry"}}
# ans_1 = nested_dict["Dakar"]["roads"]
# print(ans_1)

# # First element of the weather in Tokyp
# nested_dict = {"Tokyo": {"weather":["sunny", "cloudy"], "roads":"dry"}, "Dakar": {"weather":["foggy","windy"], "roads": "sandy"}}
# ans_1 = nested_dict["Tokyo"]["weather"][1]
# print(ans_1)
# ===================================================================================

# WHILE LOOP THAT ADDS NUMBERS IN RANGE
# Write a while loop that adds all the numbers up to 100 (inclusive).
# counter = 0
# total = 0
# while counter <= 100:
#     total = total+counter
#     counter = counter+1
# print(total)

# # Using a while loop, len function, if statement and str() function;
# # iterate through the given list and if there is a 100,
# # assign a notification message to the variable my_message with the index of 100.
# # i.e.: "There is a 100 at index no: 5"
# lst = [10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
# message = ""
# i = 0
# while i < len(lst):
#     if lst[i] == 12:
#         my_message = "There is a " + str(lst[i]) + " at index no: " + str(i)
#     i = i+1
# print(my_message)
# ======================================================

# PASS, BREAK
# # Create new list without the empty strings or any particular strings
# lst1=["Joe", "Sarah", "Mike", "Jess", "", "Matt", "", "Greg"]
# def name_adder(list):
#     i = 0
#     new_list = []
#     while i < len(list):
#         if list[i] != "":
#             new_list.append(list[i])
#         # Stop adding when "" is encountered
#         else:
#             pass # use break to stop at the occurrence of character
#         i = i+1
#     return new_list
# print(name_adder(lst1))

# # CONTINUE
# weather=["snow", "rain", "sun", "clouds"]
# for i in weather:
#     if i == "sun":
#         continue # use break to end the iteration
#     print(i)
# =========================================================================================

# SORT/SORTED METHODS, LAMBDA KEY, REVERSE, etc
# # Sort Method with key=lambda function and reverse 100/x
# # # Using .sort() method, create a lambda function that sorts the list in descending order.
# # # Refrain from using the reverse parameter.
# # (Hint: lambda will be passed to sort method's key parameter as argument)
# lst = [100, 10, 10000, 1, 9, 999, 99]
# lst.sort(key=lambda x: 100/x)
# print(lst)

# # Sorted Method with key=lambda function
# lst = [100, 10, 10000, 1, 9, 999, 99]
# lst = sorted(lst, key=lambda x: x, reverse=True)
# print(lst)

# # Using sorted() function and lambda sort the words in the list based on their second letter from a to z.
# lst=["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]
# lst = sorted(lst, key=lambda x: x[1])
# print(lst)

# # Using sorted() function and lambda sort the tuples in the list based on the second items.
# lst = [(19542209, "New York"), (4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"),
# (1805832, "West Virginia"), (39865590, "California")]
# lst = sorted(lst, key=lambda x: x[1])
# print(lst)
# ======================================================================================

# ZIP FUNCTION
# First create a range from 1 to 8. Then using zip, merge the given list
# and the range together to create a new list of tuples.
# rng1 = list(range(1, 8))
# lst1 = ["Energy", "Agriculture", "Industry", "Technology", "Finance", "Forestry", "Transport"]
# lst = list(zip(rng1, lst1))
# print(lst)
# =========================================================================================

# LAMBDA AND MAP function
# lst1=["Jane", "Lee", "Will", "Brie"]
# lst2 = list(map(lambda x: "Hello, " + x, lst1))
# print(lst2)

# Using map() function and len() function create a list
# that shows length of each element in the first list.
# lst1=["Alpine", "Avalanche", "Powder", "Snowflake", "Summit"]
# lst2 = list(map(len, lst1))
# print(lst2)

# # Using filter() and list() functions and .lower() method filter all the vowels in a given string.
# str1 = "Winter Olympics in 2022 will take place in Beijing China"
# lst = list(filter(lambda x: True if x.lower() in "aeiou" else False, str1))
# print(lst)

# # FILTER all the positive integers
# str1="Winter Olympics in 2022 will take place in Beijing China"
# lst = list(filter(lambda x: True if x in "0123456789" else False, str1))
# print(lst)

# # Using lambda and sorted() function, sort the list based on last characters of the items from z to a.
# lakes1=["Malawi", "Medicine", "Tahoe", "Moraine", "Upper Arrow", "Plitvice", "Edith", "Emerald"]
# lakes2 = sorted(lakes1, key = lambda x: x[-1], reverse = True)
# print(lakes2)

# # Using lambda and sorted() function, sort the list based on the remainder
# # from dividing each element to 5 (From greater to smaller).
# lst1 = [1000, 50, 66, 101, 333, 9999, 19, 300, 200, 250]
# lst2 = sorted(lst1, key=lambda x: x % 5, reverse=True)
# print(lst2)
# *******************************************************************
# # Given a dictionary is consisted of vehicles and their weights in kilograms.
# # Contruct a list of the names of vehicles with weight below 5000 kilograms.
# # In the same list comprehension make the key names all upper case.
# dict = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400,
#         "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# lst = [x.upper() for x in dict if dict[x] < 5000]
# print(lst)

# # Create a dictionary from the list with same key:value pairs, such as: {"key": "key"}.
# lst = ["NY", "FL", "CA", "VT"]
# dict = {x: x for x in lst}
# print(dict)

# # First, create a range from 100 to 160 with steps of 10.
# # Second, using dict comprehension, create a dictionary where each number in the
# # range is the key and each item divided by 100 is the value.
# rng= range(100, 160, 10)
# dict={x: x/100 for x in rng}
# print(dict)

# # Using dict comprehension and a conditional argument create a dictionary from the current
# # dictionary where only the key:value pairs with value above 2000 are taken to the new dictionary.
# dict1 = {"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
# dict2 = {x: dict1[x] for x in dict1 if dict1[x] > 2000}
# print(dict2)
# ===================================================================================

# # WHILE LOOP AND INPUT WITH PROMPT IMPLEMENTATION
# prompt = "\nPlease enter the name of a city you have visited;" # \n inside prompt will not break the codes
# prompt += "\n(Enter 'q for quit' when you have finished.) "
# cities = []
# while True:
#     city = input(prompt)
#     if city.lower() == 'q':
#         break
#     else:
#         cities.append(city)
# for c in cities:
#     print(f"I'd love to visit {c.title()}!")
# ====================================================================

# # LISTS ADD USER INPUT
# foods = []
# while True:
#     food = input("What food do you like?(or q to quit): ")
#     if food == "q":
#         break
#     else:
#         foods.append(food)
# print()
# print("----Your Foods List-----")
# for fd in foods:
#     print(fd.capitalize())
# =============================================

# # SHOPPING CART
# foods = []
# prices = []
# total = 0
# while True:
#     food = input("Enter a food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = int(input(f"Enter price> {food}: $"))
#         foods.append(food)
#         prices.append(price)
# print()
# print("----Your Shopping Card-----")
# for food in foods:
#     print(food.capitalize())
# for price in prices:
#     total += price
# print(f"Your total is : ${total: .2f}")
# ==========================================

# CONCESSION STAND PROGRAM
# menu = {"pizza": 3.00,
#                "nachos": 4.50,
#                "popcorn": 6.00,
#                "fries": 2.50,
#                "chips": 1.00,
#                "pretzel": 3.50,
#                "soda": 3.00,
#                "lemonade": 4.25}
# cart = []
# total = 0
#
# print("--------- MENU ---------")
# for key, value in menu.items():
#     print(f"{key:10}: ${value:.2f}")
# print("------------------------")
#
# while True:
#     food = input("Select an item (q to quit): ").lower()
#     if food == "q":
#         break
#     elif menu.get(food) is not None:
#         cart.append(food)
#
# print("------ YOUR ORDER ------")
# for food in cart:
#     total += menu.get(food)
#     print(food, end=" ")
#
# print()
# print(f"Total is: ${total:.2f}")
# ===========================================================

 # # FILLING A DICTIONARY WITH USER INPUTS
# responses = {}
# polling_active = True
# while polling_active:
#     name = input("What is your name? ")
#     response = input("Which programming language would you like to learn? ")
#     responses[name] = response # stores above response in a dictionary
#     repeat = input("Another response? (yes/no)")
#     if repeat.lower() == "no":
#         polling_active = False
#     #     break
#     # else:
#     #     print("Programming is fun. Gotta learn it")
#
# print("\n------ Poll Results -------")
# for name, response in responses.items():
#     print(f"{name} would like to learn {response}.")
# =============================================================================

# # LOOP OVER TWO LISTS
# names = ["Eiffel Tower", "Empire State", "Tokyo Tower"]
# heights = [324, 381, 400]
# for i in range(len(names)):
#     name = names[i]
#     height = heights[i]
#     print(f"{name:12}: {height} meters")
# ====================================================================================
