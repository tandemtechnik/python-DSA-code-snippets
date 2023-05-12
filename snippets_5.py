"""
COMMON ELEMENTS
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
# print(even_nums, common_values)
# # ***************************************
# # if set(even_nums).intersection(lst):
# #     print('Lists have elements in common')
# # else:
# #     print('No elements in common')
# ***************************************************
"""
LISTS SUBSET -- INTERSECTION
Given two lists A and B, write a Python program to Check if list A is contained in list B without breaking A’s order. 
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
#     #using this code - lst3 = [value for value in lst1 if value in lst2]
#     return lst3
#
# # example of two lists to test the intersection program
# lst1 = [1,2,2,1]
# lst2 = [2,2]
# # print the final output
# print(intersection(lst1, lst2))
# ======================================================================================

# # Finding numbers smaller than both left & right neighbours:
# lis = [5,3,4,6,2,7,1,8]
# output = []
# for i in range(len(lis)-2):
#     left = lis[i]
#     # print(left)
#     this = lis[i+1]
#     # print(this)
#     right = lis[i+2]
#     # print(right)
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
"""
SNIPPETS_4: 127
"""
# lst = [1, 5, 7, 8, 4]
# total = 0
# for i, j in zip(lst, lst[1:]):
#     add_ = i + j
# #    print(i, j)
# #   print(add_)
#     total += add_
# print(total)
# # =======================================================================

# # Combining consecutive strings together:
# lis = ["apple", "orange", "pear", "durian"]
# output = []
# for i in range(len(lis)-1):
#     this = lis[i]
#     next = lis[i+1]
#     output.append(this + " " + next)# ["apple orange", "orange pear", "pear durian"]
# print(output)

