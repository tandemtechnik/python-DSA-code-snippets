"""
COMMON EVEN NUMBER ELEMENTS
---------------------------
LIST INTERSECTION
CUSTOM ITERATIONS --- BRUTE FORCE
CODING CHALLENGE ----- solve
collect all the even numbers into a variable
compare which elements in the variable are in the targets list
Find values of even numbers in one list that is present in another list
And also, just show True/False
"""


# nums = [72, 40, 38, 25, 20, 23, 51, 49]
# lst = [73, 72, 38, 25, 20, 90, 72, 22, 44]
# def common_evens(nums):
#     evens = []
#     for n in nums:
#         if n % 2 == 0:
#             evens.append(n)
#     return evens
# even_nums = common_evens(nums)
# common_values = [i for i in even_nums if i in lst]
# # common_values = [i for i in even_nums if i not in lst]
# # common_values = [i for i in nums if i in lst]
# # print(common_values)
# print(f"Even numbers: {even_nums}, Common values: {common_values}")
# # ***************************************
# # if set(even_nums).intersection(lst):
# #     print('Lists have elements in common')
# # else:
# #     print('No elements in common')
# ***************************************************
"""
LISTS SUBSET -- INTERSECTION
Given two lists A and B, write a Python program to Check if list A is contained in list B 
without breaking A’s order. 
"""
# def is_sublist(A, B):
#     if not A:
#         return True
#     if not B:
#         return False
#     if A[0] == B[0]:
#         return is_sublist(A[1:], B[1:])
#     return is_sublist(A, B[1:])
# A = [1, 2]
# B = [1, 2, 3, 1, 1, 2, 2]
# result = is_sublist(A, B)
# print(result)
# *******************************************
"""
LIST INTERSECTION
BRUTE FORCE METHOD
a function to find intersection of two lists
"""
# def intersection(lst1, lst2):
#     # a new list to keep track of common elements in lst1 and lst2
#     lst3 = []
#     #iterate over all elements in lst1
#     for value in lst1:
#         #check for each element of lst1 if it's present in lst2
#         if value in lst2:
#             #if true, add the common element to the new list
#             lst3.append(value)
#     #we can shorten the four lines of code above
#     #using this code ----
#     # lstx = [value for value in lst1 if value in lst2]
#     # return lstx
#     return lst3
#
# # example of two lists to test the intersection program
# lst1 = [1,2,5,1]
# lst2 = [5,2]
# # print the final output
# print(intersection(lst1, lst2))
# ======================================================================================

# # Finding numbers smaller than both left & right neighbours:
# lis = [5,3,4,6,2,7,1,8]
# output = []
# for i in range(len(lis)-2):
#     left = lis[i]
#     this = lis[i+1]
#     right = lis[i+2]
#     if this < left and this < right:
#         output.append(this)# [3,2,1]
# print(output)
# ====================================================================
"""
SUM OF CONSECUTIVE TWO ELEMENT IN ARRAY
Finding the sum of consecutive two elements in an array of numbers
"""
# lis = [1,10,100,1000,10000]
# output = []
# sum_ = 0
# for i in range(len(lis)-1):
#     this = lis[i]
#     next = lis[i+1]
#     output.append(this+next)# [11,110,1100,11000]
# for i in output:
#     sum_ += i
# print(output, sum_)
# ************************************

# # Combining consecutive strings together:
# lis = ["apple", "orange", "pear", "durian"]
# output = []
# for i in range(len(lis)-1):
#     this = lis[i]
#     next = lis[i+1]
#     output.append(this + " " + next)# ["apple orange", "orange pear", "pear durian"]
# print(output)
# ***********************************************

# # SUM OF CONSECUTIVE TWO ELEMENT IN ARRAY ----- TURING CODING CHALLENGE
# lst = [1, 5, 7, 8, 4]
# total = 0
# for i, j in zip(lst, lst[1:]):
#     add_ = i + j
# #    print(i, j)
# #   print(add_)
#     total += add_
# print(total)
# ========================================================

# # SUM OF CONSECUTIVE TWO ELEMENT IN ARRAY
# # my_list = [41, 27, 53, 12, 29, 32, 16]
# my_list = [1, 5, 7, 8, 4]
# # print("The list is :")
# # print(my_list)
# total = 0
# # my_result = [a + b for a, b in zip(my_list, my_list[1:] + [my_list[0]])]
# sums = [a + b for a, b in zip(my_list, my_list[1:] + [my_list[0]])]
# for i in sums:
#     total += i
# # print(f"Result: {my_result}. Total: {sum}")
# print("Sums: ",sums)
# print("Total: ",total)

# ==================================================================

# # Turing coding challenge
# input = "*************"
# el_1 = input[:2]
# el_2 = input[3:]
# output = [el_1.replace("*", "-")] + [el_2]
# # print(el_1)
# # print(el_2)
# print(output)
# *****************************************

# # CODING CHALLENGE
# age = 17
# if age >= 18 or ...:
#     print("I'm going to drive on my own")
# else:
#     print("I need a driver")
# =====================================================================

# from itertools import dropwhile
# def func(array):
#     filtered_list = dropwhile(lambda x:x < 0, array)
#     return filtered_list
# numz = [-3, -2, -1, 0, 1, 2, 3]
# result = func(numz)
# next(result)
# print(next(result))
# *********************************
# def zip_func(list1, list2):
#     zipped = zip(list1, list2)
#     result = [(a, b) for a, b in zipped if a != b]
#     return *result,
# list1 = [1, 2, 3, 4, 5]
# list2 = [1, 3, 3, 4, 6]
# output = zip_func(list1, list2)
# print(output)
# ***************************************
# langs = ["java", "C++", "Rust"]
# # for lang in langs:
# langs.append("Python")
# print(langs)
# ****************************************

# def my_func(value):
#     if value == 5:
#         return ["Python"]
#     else:
#         yield from range(value)
# print(list(my_func(5)))
# ===============================================
"""
By default all objects are true unless they are mentioned as false. 
So the else condition is compiled and it gives a list of even numbers.
"""
# result = [x for x in range(10) if x % 2 != 0] if False else [x for x in range(10) if x % 2 == 0]
# print(result)
# ===================================================

# snakes = ["Python", "Cobra", "Anaconda"]
# snakes.extend("Boa")
# print(snakes)
# # ******************************

# # Rounds off to the nearest even number
# def round_off():
#     num1 = round(9/2)
#     num2 = round(7/2)
#     return num1, num2
#     # return num1 == num2
# print(round_off())
# **************************************

# def process_data(data):
#     unique_values = set()
#     all_values = ()
#
#     for item in data:
#         unique_values.add(item)
#         all_values += (item,)
#         return unique_values in all_values
# data = [1, 2, 3, 2, 4, 5, 3, 6]
# print(process_data(data))
# **************************************

# a = [1, 2, 3]
# b = a.append(4)
# print(a, b)
# ****************************************
#
# a = [1, 2, 3]
# b = a
# b[1] = 4
# print(a, b)
# ******************************************

# my_list = []
# my_list += "Python"
# print(my_list)
#
# my_list = []
# my_list.append("Python")
# print(my_list)
# *******************************************

# import pathlib
# desktop = pathlib.Path("Downloads")
# for item in desktop.rglob("*"):
#     if item.is_file():
#         print(item)

# [item for item in desktop.rglob("*") if item.is_file()]

# list(filter(lambda item: item.is_file(), desktop.rglob("*")))
# *********************************************
#
# # Second Largest number in a list
# def find_second_largest(lst):
#     first, second = float('-inf'), float('-inf')
#     for num in lst:
#         if num > first:
#             first, second = num, first
#         elif first > num > second:
#             second = num
#     return second
# my_nums = [44, 11, 83, 29, 25, 76, 88]
# second_largest = find_second_largest(my_nums)
# print(f"The second largest number is: {second_largest}")
# # *****************************************************

# lst = [1, 2, 3, 4]
# for idx, nums in enumerate(lst):
#     # del(nums)
#     print(idx, nums) #(f"{idx}: {nums}")
# print(lst)
# ***********************************
# for idx, num in enumerate(range(1,13)):
#     print(f"{idx:5}: {num}")
# ***********************************
# for num in range(1,11):
#     punishment = ("I'm sorry Ma'am!")
#     print(f"{num:5}: {punishment}")
# # ************************************************

# # GREATEST COMMON DIVISOR
# # Recursive function to return gcd of a and b
# def gcd(a, b):
#     # Edge cases
#     if (a == 0):
#         return b
#     if (b == 0):
#         return a
#     # base case
#     if (a == b):
#         return a
#     # a is greater
#     if (a > b):
#         return gcd(a-b, b)
#     return gcd(a, b-a)
# print(gcd(8, 12))
# # 	print('GCD of', a, 'and', b, 'is', gcd(a, b))
# # else:
# # 	print('not found')
# # import math
# # print(math.gcd(15, 45))
# # **************************************************
# def func(x):
#     x *= 2
#     # return x
# num = 15 and 6
# print(num)
# # print(func(num))
# **************************************************

# def modify_str():
#     str1 = ("I Love Python")
#     # str1 = str1.replace("Love", "Enjoy").split()
#     return str1
# print(modify_str())
