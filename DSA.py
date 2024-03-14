k = ["3", "6", "2", "4", "1", "5"]
v = ["love", "computers", "dogs", "cats", "I", "you"]
#
# my_dict = {}
# for k, v in zip(k, v):
#     my_dict[k] = v
# print(my_dict)

# my_dict = {k: v for k, v in zip(k[[3][5]], v)}
# print(my_dict)


# #
# mydict = {
# "3": "love",
# "6": "computers",
# "2": "dogs",
# "4": "cats",
# "1": "I",
# "5": "you"
# }
#
# dict1 = {k : v for k,v in mydict.items() if k in [2,3]}
# print(dict1)
# for k, v in mydict:
#     (mydict[])

# sorted_by_keys = dict(sorted(mydict.items()))
#
# sorted_by_values = filter(mydict, [1])
# print(sorted_by_values)
# print(sorted_by_keys)


# def marital_status(name):
#     return marital_status_dict.get(name, 'unknown')
# print(marital_status("John"))

# def marital_status(name):
#     return marital_status_dict.items(self=2)
# print(marital_status("John"))

# # Babylonian Method
# class Solution():
#     def mySqrt(self, x: int) -> int:
#         if x <= 1:
#             x
#         else:
#             x_n = 0.5 * x
#             change = 1
#             while change > 0.1:
#                 next_n = 0.5 * (x_n + x/x_n)
#                 change = abs(x_n - next_n)
#                 x_n = next_n
#             return(int(x_n))
# sol = Solution()
# result = sol.mySqrt(49)
# print(result)
#
# # Exponent solution
# a=int(input("enter no."))
# b=a**0.5
# print(b)
#
# # import solution
# import math
# x = int(input())
# import math
# print(pow(x, 0.5))
# # or,
# print(x**0.5)

# Best solution
# num = float(input("Enter num: "))
# a = 1.0
# while(1):
#     b = a*a
#     if  num-0.1 < b < num+0.1:
#         break
#     else:
#         pass
#     a = a + 0.01
# print("\n Square root value is: ",round(a,2))

# Function to shuffle an array of size 2n
# def shuffleArray(a, n):
#
# 	# Rotate the element to the left
# 	i, q, k = 0, 1, n
# 	while(i < n):
# 		j = k
# 		while(j > i + q):
# 			a[j - 1], a[j] = a[j], a[j - 1]
# 			j -= 1
# 		i += 1
# 		k += 1
# 		q += 1
#
# a = [1, 3, 5, 7, 2, 4, 6, 8]
# n = len(a)
# shuffleArray(a, int(n / 2))
# for i in range(0, n):
# 	print(a[i], end = " ")

# import random
# secret_number = random.randint(1, 6)
# while True:
#     guess = int(input("Enter a number between 1 to 50 >> "))
#     if guess == secret_number:
#         print("Congrats! You got it")
#         break
#     elif guess > secret_number:
#         print("Too high! Try again")
#     else:
#         print("Too low! Try again")


# # *********************************************************
# d = {
# "3": "love",
# "6": "computers",
# "2": "dogs",
# "4": "cats",
# "1": "I",
# "5": "you"
# }
# # # d = {1:11, 2:22, 3:33}
# # #
# # # # filter by key
# # # # d2 = {k : v for k,v in filter(lambda t: t[0] in [1, 3], d.iteritems())}
# # # # print(d2)
# # # # filter by value
# # d3 = {k : v for k,v in d.items() if k in ["1","3"]}
# # print(d3)
# # # **********************************************************************************

# # Function to demonstrate printing pattern of numbers
# def pattern_num(n):
#     # initializing starting number
#     num = 1
#     lst = []
#     # outer loop to handle number of rows
#     for i in range(0, n):
#         print(" " * (n - i), end="") # forms equilateral triangle
#
#         # not re assigning num
#         # num = 1
#
#         # inner loop to handle number of columns
#         # values changing acc. to outer loop
#         for j in range(0, i + 1):
#             # printing number
#             print(num, end=" ")
#             lst.append(num)
#
#             # incrementing number at each column
#             num = num + 1
#
#
#         # ending line after each row
#         print("\r")
#     # for k in range(0, i + 1):
#     #     lst.append(num)
#     # print(lst)
#     # print(lst[0])
#     # lst = [0,2,5]
#     # for i in range(n):
#     lst.append(i)
#     # lst = lst
#     # return lst
#     # print(lst)
#     d = ["I", "dogs", "love", "cats", "you", "computers"]
#     dict = {lst: d for lst, d in zip(lst, d)}
#     lstvals = list(dict.values())
#     nlist = [x for x in lstvals if "dogs" not in x and "cats" not in x and "you" not in x]
#     nlistToStr = ' '.join([str(elem) for elem in nlist])
#
#     # print(nlist)
#     # print(dict)
#     print(nlistToStr)
#
#     # produce I love computers here
#
# # n = 3
#
# # sending 3 as argument
# # calling Function
# pattern_num(3)
# ====================================================================



# Another list above. Zip both d and lst to produce a dict below, then comprehension to achieve result
# result = I love computers
# d = {
# "3": "love",
# "6": "computers",
# "2": "dogs",
# "4": "cats",
# "1": "I",
# "5": "you"
# }

# # # Python program to print a pyramid pattern of stars
#
# #
# # n=10
# # for i in range(1,n+1):
# #     print(" "*(n-i),end="")
# #     for j in range(1,i+1):
# #         print(j,end=" ")
# #     print()

# equation = '160 + 135 = 295'
# # symbol: str = ''
# # output: str = ''
#
# for symbol in equation:
#     if symbol in '12':
#         # output += symbol
#
# # print(output)
#         print(symbol)
#
#

# d = {'a': 10, 'b': 20, 'c': 30}
# d1 = {k for (k,v) in d.items() if 'a'|'b' in k}
# print(list(d.values()[2]))
# print(d.get('b'))
# print(d.get('z'))
#
# def checkinf(value):
#     if value in a:
#         print(value)
#
# def find_max(nums):
#     max_num = nums[0] # float("-inf") # smaller than all other numbers
#     for num in nums:
#         if num > max_num:
#             max_num = num
#     return max_num
# nums = [2, 6, 8, 9]
# print(find_max(nums))

# divv = 11//2
# print(divv)

# for i in '123':
#     print (i, "guru99")

# Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
# print("Students Name: %s" % list(Dict.items()))
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "apple" not in x and  "cherry"  not in x]
#
# print(newlist)


# c_num = 3j + 10
# print("The type is : ",type(c_num))

# my_list = [1, 2, 3, 4, 5]
# new_list = my_list[1:4]
# new_list[0] = 9
# print(new_list)
# print(my_list)

# name = input("Enter your name: ")


# name = "Close"
# asci = []
# for c in name:
#     asci.append(ord(c))
# print(f"The ASCII for Close is: {asci} \nSolution:")
# total = 0  # initialize a running total to 0
# for i in asci:  # for each i in the asci list
#     total += i  # add i to the running total
#     print(total, end=" ")  # print the running total elements
#
# newlist = [2,5,9,12,50]

# for i in range(1,len(asci)):
#     print(sum(asci[:i+1]))

# name = "Close"
# asci = []
# for c in name:
#     asci.append(ord(c))
# for i in range(0,len(asci)):
#     print(sum(asci[:i+1]))

# input_string = '"Hello"World"Hello"'
# print(input_string)

# def is_palindrome(s):
#     reversed_s = s[::-1]
#     if s == reversed_s:
#         return s == reversed_s
# s = "radar"
# print(is_palindrome(s))

"""
Given an array of integers a, your task is to find how many of its contiguous subarrays of length m contain a pair of 
integers with a sum equal to k. More formally, given the array a, your task is to count the number of 
indices 0 ≤ i ≤ a.length - m such that a subarray [a[i], a[i + 1], ..., a[i + m - 1]] contains at least one 
pair (a[s], a[t]), where:

s ≠ t
a[s] + a[t] = k
Example

For a = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7], m = 4, and k = 10, the output should be solution(a, m, k) = 5.

Let's consider all subarrays of length m = 4 and see which fit the description conditions:

Subarray a[0..3] = [2, 4, 7, 5] doesn't contain any pair of integers with a sum of k = 10. 
Note that although the pair (a[3], a[3]) has the sum 5 + 5 = 10, it doesn't fit the requirement s ≠ t.
Subarray a[1..4] = [4, 7, 5, 3] contains the pair (a[2], a[4]), where a[2] + a[4] = 7 + 3 = 10.
Subarray a[2..5] = [7, 5, 3, 5] contains two pairs (a[2], a[4]) and (a[3], a[5]), both with a sum of k = 10.
Subarray a[3..6] = [5, 3, 5, 8] contains the pair (a[3], a[5]), where a[3] + a[5] = 5 + 5 = 10.
Subarray a[4..7] = [3, 5, 8, 5] contains the pair (a[5], a[7]), where a[5] + a[7] = 5 + 5 = 10.
Subarray a[5..8] = [5, 8, 5, 1] contains the pair (a[5], a[7]), where a[5] + a[7] = 5 + 5 = 10.
Subarray a[6..9] = [8, 5, 1, 7] doesn't contain any pair with a sum of k = 10.
So the answer is 5, because there are 5 contiguous subarrays that contain a pair with a sum of k = 10.

For a = [15, 8, 8, 2, 6, 4, 1, 7], m = 2, and k = 8, the output should be solution(a, m, k) = 2.
"""

#
#
# # arr, k, target = [15, 8, 8, 2, 6, 4, 1, 7], 2, 8  # 2
# arr, k, target = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7], 4, 10
#
#
# elems = {}  # SW hashmap
# last_pair_start = -1  # max start of any pair
# count = 0  # result
#
# for i in range(k):
#     complement = target - arr[i]
#     if complement in elems:
#         last_pair_start = max(last_pair_start, elems[complement])
#     # keep track of the last found index for this element
#     elems[arr[i]] = i
#
#     if last_pair_start != -1:
#         # pair exists
#         count += 1
#
# for i in range(k, len(arr)):
#     idx_removed = (i - k)
#
#     if elems[arr[idx_removed]] == idx_removed:
#         # all traces of this element have been removed
#         del elems[arr[idx_removed]]
#
#     if idx_removed == last_pair_start:
#         # we lost our last pair
#         last_pair_start = -1
#
#     complement = target - arr[i]
#     if complement in elems:
#         # saving complement's index because we are moving forward
#         # this pair's gonna last as long as this index does
#         last_pair_start = max(last_pair_start, elems[complement])
#
#     elems[arr[i]] = i
#
#     if last_pair_start != -1:
#         count += 1
#
# print(count)