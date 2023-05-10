"""
Anagrams
are words formed by rearranging the letters of another word, For example, car and arc, cat and act, etc.
Grouping anagrams is one of the popular questions in coding interviews.
"""
# from collections import defaultdict
# def group_anagrams(a):
#     dfdict = defaultdict(list)
#     for i in a:
#         sorted_i = " ".join(sorted(i))
#         dfdict[sorted_i].append(i)
#     return dfdict.values()
# words = ["tea", "eat", "bat", "ate", "arc", "car"]
# print(group_anagrams(words))
# ================================================================================
"""
EXECUTION TIME
The execution or running time of the program indicates how quickly the output is delivered based on the algorithm
you used to solve the problem. To calculate the execution time of the program, we need to calculate the time taken
by the program from its initiation to the final result.
So to calculate the execution time of a Python program, we need to follow the steps mentioned below:
*First, store the time of initiation of the program into a variable;
*Write the Python program;
*Store the end time of the program into a variable;
*Subtract the time of initiation of the program from the end time of the program;
"""
# from time import time
# start = time()
"""
==============================
CREATE ACRONYMS
Python program to create acronyms
================================
"""
# word = "Internet of Things"
# text = word.split()
# a = " "
# for i in text:
#     a = a+str(i[0]).upper()
# print(a)
# =======================================
# end = time()
# execution_time = end - start
# print(f"Execution Time :  {execution_time}")
# ==========================================================================================

# # COUNT MOST FREQUENT WORDS IN A FILE
# words = []
# with open("aman.txt", "r") as f:
#     for line in f:
#         words.extend(line.split())
# from collections import Counter
# counts = Counter(words)
# top_n = counts.most_common(3)
# print(top_n)
# ===============================================================================================

# SHOW MOST FREQUENT WORDS IN A LIST
# def most_freq(List):
#     counter = 0
#     num = List[0]
#     for i in List:
#         curr_freq = List.count(i)
#         if(curr_freq > counter):
#             counter = curr_freq
#             num = i, counter
#     return num
# # List = [2, 4, 6, 2, 8, 2]
# List = ["tboy", "sophia", "grandma", "sophia", "babaay", "dad", "sophia", "sophia"]
# print(most_freq(List))
# =======================================================================================

# #  COUNT CAPITAL LETTERS IN A FILE
# with open("aman.txt") as file:
#     count = 0
#     text = file.read()
#     for i in text:
#         if i.isupper():
#             count += 1
#     print(count)
# =========================================================================================

# #FUNCTIONS
# # Higher Order Functions
# def square(x):
#     return x*x
#
# def cube(x):
#     return x*x*x
#
# def my_map(func, my_list):
#     result = []
#     for i in my_list:
#         result.append(func(i))
#     return result
#
# squares = my_map(square, [1, 2, 3, 4, 5])
# cubes = my_map(cube, [1, 2, 3, 4, 5])
#
# print(squares)
# print(cubes)
# =============================================================================

# # CLOSURES
# def logger(msg):
#
#     def log_message():
#         print('Log:', msg)
#     return log_message()
# msg = "You have been punked!"
# logger(msg)
# ============================================================================
"""
MAXIMUM VALUE
Maximum value in a python list or infact in any iterable without using max() function
"""
# my_list = [2,3,1,4,6,7,99,999,88]
# # max_ = max(my_list)
# # print(max_)
# max_num = None
# for num in my_list:
#     if max_num is None or max_num < num:
#         max_num = num
# print(max_num)
# my_list = [2,3,1,4,6,7,99,999,88]
# *************************************
## MINIMUM VALUE
# min_num = None
# for num in my_list:
#     if min_num is None or num < min_num:
#         min_num = num
# print(min_num)
# ***************************************
## MINIMUM VALUE WITH FUNCTION
# def minimum(list):
#     curr_min = list[0]
#     for num in list:
#         if curr_min > num:
#             curr_min = num
#             return curr_min
# print(minimum([2,3,1,4,6,7,99,999,88]))
# **********************************************
# my_list = [2,3,1,4,6,7,99,999,88]
# max_num = my_list[0]
# for num in my_list:
#     if num > max_num:
#         max_num = num
# print(max_num)
# print(a.index(max_num))
# **********************************************
# my_list = [2,3,1,4,6,7,99,999,88]
# min_num = my_list[0]
# for num in my_list:
#     if min_num > num:
#         min_num = num
# print(min_num)
# ==================================================
"""
FIND THE INDEX OF MAXIMUM VALUE IN A LIST
Also if you want to find the index of the resulting max,
"""
# def maximum(x):
#     maximum_index = 0
#     current_index = 1
#     while current_index < len(x):
#         if x[current_index] > x[maximum_index]:
#             maximum_index = current_index
#         current_index += 1
#     return maximum_index
# a = [23, 76, 45, 20, 70, 165, 15, 54]
# print(maximum(a))
# ******************************************************
# def minimum(x):
#     minimum_index = 0
#     current_index = 1
#     while current_index < len(x):
#         if x[current_index] < x[minimum_index]:
#             minimum_index = current_index
#         current_index += 1
#     return minimum_index
# a = [23, 76, 45, 20, 7, 65, 15, 54]
# print(minimum(a))
#======================================================================================
"""
DISTANCE BETWEEN TWO LOCATIONS
Calculating the distance between two locations helps companies like Swiggy and Zomato calculate the delivery time
for an order.
How to Calculate Distance Between two Locations?
We can use the haversine formula to calculate the distance between two locations. The haversine formula calculates the
distance between two latitude and longitude points. This formula is defined as:
haversine(d/R) = haversine(latitude2- latitude1 + cos(latitude1 * cos(latitude2 * haversine(longitude2 – longitude1)
In this formula:
d is the distance between the two points
r is the radius of the earth
and haversine is the haversine function defined as:
haversine(theta) = sin^2(theta/2)
To calculate the final distance in kilometres, you need to multiply the distance between the two points by the radius of
the earth.
"""
# import numpy as np
# # Set the earth's radius (in kilometers)
# r = 6371
#
# # Convert degrees to radians
# def deg_to_rad(degrees):
#     return degrees * (np.pi/180)
#
# def distcalculate(lat1, lon1, lat2, lon2):
#     d_lat = deg_to_rad(lat2-lat1)
#     d_lon = deg_to_rad(lon2-lon1)
#     a = np.sin(d_lat/2)**2 + np.cos(deg_to_rad(lat1)) * np.cos(deg_to_rad(lat2)) * np.sin(d_lon/2)**2
#     c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
#     return r * c
#
# # Now let’s calculate the distance between two locations with the function we just defined above:
#
# print(distcalculate(22.745049, 75.892471, 22.765049, 75.912471))
# ==================================================================================================

# # REMOVE FUNCTION
# languages = ['Java', 'C++', 'Python', 'Javascript', 'Julia', 'Rust']
# for lang in languages[:]:
#     languages.remove(lang)
# print(languages)
# ==============================================================================================
"""
COUNTDOWN
With Sleep() function
"""
# import time
# for count_down in range(10, 0, -1):
#     print(count_down)
#     time.sleep(1)
# print("Happy Birthday Mommy!!!")
# =====================================================================================
"""
NUMBER GUESSING GAME
Implement Binary Search Method
"""
# import random
# secret_number = random.randint(1, 20)
# while True:
#     guess = int(input("Guess the number between 1 and 20: "))
#     if guess == secret_number:
#         print("Congratulations! You got it!")
#         break
#     elif guess < secret_number:
#         print("Too low! Try again.")
#     else:
#         print("Too high! Try again.")
# =========================================================================================
"""
PASSWORD GENERATOR
This function generates a random password of a given length using a combination of
uppercase letters, lowercase letters, digits, and special characters
"""
# import random
# import string
# def generate_password(length):
#     # Define a string containing all possible characters
#     all_chars = string.ascii_letters + string.digits + string.punctuation
#     # Generate a password using a random selection of characters
#     password = "".join(random.choice(all_chars) for i in range(length))
#     return password
# # Test the function by generating a password of length 8
# password = generate_password(8)
# print(password)
# ***************************************************
"""
PASSWORD CHECKER
The Password Checker is to check if a password is strong enough based on some of the criteria we set. 
It'll print an error if any of the password criteria isn't met.
"""
# def password_checker(password):
#     # Define the criteria for a strong password
#     min_length = 8
#     has_uppercase = False
#     has_lowercase = False
#     has_digit = False
#     has_special_char = False
#     special_chars = "!@#$%^&*()-_=+[{]}\|;:',<.>/?"
#
#     # Check the length of the password
#     if len(password) < min_length:
#         print("Password is too short!")
#         return False
#
#     # Check if the password contains an uppercase letter, lowercase letter, digit, and special character
#     for char in password:
#         if char.isupper():
#             has_uppercase = True
#         elif char.islower():
#             has_lowercase = True
#         elif char.isdigit():
#             has_digit = True
#         elif char in special_chars:
#             has_special_char = True
#
#     # Print an error message for each missing criteria
#     if not has_uppercase:
#         print("Password must contain at least one uppercase letter!")
#         return False
#     if not has_lowercase:
#         print("Password must contain at least one lowercase letter!")
#         return False
#     if not has_digit:
#         print("Password must contain at least one digit!")
#         return False
#     if not has_special_char:
#         print("Password must contain at least one special character!")
#         return False
#
#     # If all criteria are met, print a success message
#     print("Password is strong!")
#     return True
#
# # Prompt the user to enter a password and check if it meets the criteria
# password = input("Enter a password: ")
# password_checker(password)
# ====================================================================================
"""
WEB SCRAPPER
How to Build a Web Scraper in Python
A web scraper scrapes/gets data from webpages and saves it in any format, either .csv or .txt.
We will build a simple web scraper in this section using a Python library called Beautiful Soup.
"""
# import requests
# from bs4 import BeautifulSoup
#
# # Set the URL of the webpage you want to scrape
# url = 'https://holypython.com/intermediate-python-exercises/exercise-20-pass-statement/'
#
# # Send an HTTP request to the URL and retrieve the HTML content
# response = requests.get(url)
#
# # Create a BeautifulSoup object that parses the HTML content
# soup = BeautifulSoup(response.content, 'html.parser')
#
# # Find all the links on the webpage
# links = soup.find_all('a')
#
# # Print the text and href attribute of each link
# for link in links:
#     print(link.get('href'), link.text)
# =========================================================================================
"""
CURRENCY CONVERTER
Explanation:
In this code, we define a function called currency_converter() that takes an amount, source currency code,
and target currency code as arguments and returns the converted amount.
We first set the API endpoint for currency conversion using the from_currency parameter and the requests
module to send a GET request to the endpoint.
We then extract the exchange rate for the target currency from the JSON data returned by the API using the
to_currency parameter and calculate the converted amount by multiplying the exchange rate with the amount
parameter.
Finally, we prompt the user to enter the amount, from_currency, and to_currency using the input() function
and pass them to the currency_converter() function to convert the currency. The converted amount is then
printed using string formatting.
"""
# # Import the necessary modules
# import requests
#
# # Define a function to convert currencies
# def currency_converter(amount, from_currency, to_currency):
#     # Set the API endpoint for currency conversion
#     api_endpoint = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
#
#     # Send a GET request to the API endpoint
#     response = requests.get(api_endpoint)
#
#     # Get the JSON data from the response
#     data = response.json()
#
#     # Extract the exchange rate for the target currency
#     exchange_rate = data["rates"][to_currency]
#
#     # Calculate the converted amount
#     converted_amount = amount * exchange_rate
#
#     # Return the converted amount
#     return converted_amount
#
# # Prompt the user to enter the amount, source currency, and target currency
# amount = float(input("Enter the amount: "))
# from_currency = input("Enter the source currency code: ").upper()
# to_currency = input("Enter the target currency code: ").upper()
#
# # Convert the currency and print the result
# result = currency_converter(amount, from_currency, to_currency)
# print(f"{amount} {from_currency} is equal to {result} {to_currency}")
# ======================================================================================

# COMPARE WITH PYTHON is, and ==
# class Compare:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __bool__(self):
#         return self.a is self.b
#         # return self.a == self.b
#
# cl = Compare([1, 2, 3], [1, 2, 3])
# print(cl.__bool__())
# ========================================================================================

# # LIST TRICKS AND TIPS
# def tricky_list(lst):
#     return lst[:-1] and lst[:-2]
#     if True:
#         len(lst[1]) == len(lst[-1])
#     else:
#         lst[1:]
# names = ["Ben", "Ken", "Len"]
# print(tricky_list(names))
# ===========================================================================================
"""
DICTIONARY CREATION
Create a dictionary from 2 lists
"""
# names = ["Joe", "James", "John", "Jason"]
# ages = [34, 37, 22, 55]
# dict = {name: age for name, age in zip(names, ages)}
# print(dict)
# ==============================================================================================

# # PRIME NUMBER CHECKER
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(2))
# print(is_prime(17))
# print(is_prime(5))
# print(is_prime(22))
# print(is_prime(48))
# =============================================================================================

# # Most common letter in one liner code
# s = "learning python with codingmantras"
# print(max(s, key=s.count))
# =========================================================================

# STRING SLICING
# # Reversed String
# s = "Tandem Techniques"
# reversed_string = s[::-1]
# print(reversed_string)
# ==============================================================================

# # VARIABLE VALUES FOR IS AND ==
# x = [1, 2, 3]
# y = [1, 2, 3]
#
# a = "hello"
# b = "hello"
#
# print(x is y)
# print(a is b)
# print(x == y)
# print(a == b)

# False
# True
# True
# True
# ==================================================================================

# CLASSES
# # CLASS INSTANCES
# class User:
#     #Constructor
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return f"Hello, my name is {self.name}"
# #Class Instances
# user1 = User("Tboy")
# user2 = User("Babaay")
#
# print(user1.greet())
# print(user2.greet())

# class student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# *************************************************************
# class student_marks:
#     def __init__(self, name, english, maths, science, sst):
#         self.name = name
#         self.english = english
#         self.maths = maths
#         self.science = science
#         self.sst = sst
#
#     def calculate_avg_marks(self):
#         total_marks = self.english + self.maths + self.science + self.sst
#         avg_marks = total_marks / 4
#         return avg_marks
# student1 = student_marks("Ashwini", 20, 12, 14, 15)
# student2 = student_marks("Ashu", 10, 18, 16, 9)
# student3 = student_marks("Sonu", 16, 14, 20, 11)
# student4 = student_marks("Sushant", 20, 20, 20, 20)
#
# print(student1.calculate_avg_marks())
# print(student2.calculate_avg_marks())
# print(student3.calculate_avg_marks())
# print(student4.calculate_avg_marks())
# # ================================================================

# FUNCTIONS
# # REPLACE FUNCTION
# s = "awesome"
# print(s.replace('e', 'r', 1))
# # Only one instance of e is replaced in this case
# *********************************
# def multiply(a, b):
#     result = a * b
#     return result
# result = multiply(2, 7)
# print(result)
# result = [a*b for a, b in (2, 7)]
# result = (lambda a, b: a * b)(2, 7)
# print(result)
# **********************************
# CODING CHALLENGE
# org_list = [1, 2, 3, 4, 5]
# fin_list = []
# for num in org_list:
#     fin_list.append(num**3)
# print(fin_list)
# ===============================================================

# # VOWELS ONLY
# def only_vowels(word: str) -> bool:
#     word = word.lower()
#     vowels = 'aeiou'
#     return all(c in vowels for c in word)
# print(only_vowels("Ada"))
# print(only_vowels("Eai"))
# ====================================================================

# # COLLECTIONS
# my_list = [i * i for i in range(5)]
# print(my_list)
# my_tuple = (i * i for i in range(5))
# print(my_tuple) # immutable collection
# my_set = {i * i for i in range(5)}
# print(my_set)
# my_dict = {i: i * i for i in range(5)}
# print(my_dict)
# ====================================================================

# # ZIP
# firsts = ['Harry', 'Ron', 'Hermione']
# lasts = ['Potter', 'Weasley', 'Granger']
# names = [f"{first} {last}" for first, last in zip(firsts, lasts) if len(firsts) == len(lasts)]
# print(names)
# =========================================================================

# CODING CHALLENGE
# i = j = [3]
# i += j
# print(i, j)
# [3,3] [3,3]
# j is an instance of i both pointing to same address
# *****************************************************
# i = j = "Python"
# i += "rocks!"
# print(i, j)
# # Pythonrocks!, Python
# # j is an instance of i both pointing to same address
# ===========================================================================

# Fizz Buzz
# for num in range(1, 16):
#     if num % 5 == 0 and num % 3 == 0:
#         print("FIZZBUZZ")
#     elif num % 5 == 0:
#         print("FIZZ")
#     elif num % 3 == 0:
#         print("BUZZ")
#     else:
#         print(num)