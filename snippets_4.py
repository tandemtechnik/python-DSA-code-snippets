# https://www.turing.com/interview-questions/python#advanced
# def increment_by(n, increment=1):
#     return n + increment
# result = increment_by(5, 4)
# # result = increment_by(4)
# print(result)
# The functions work like this:
# increment_by(5, 2)
# increment_by(4)
# ========================================================================

#Declaring lists
# list1=['a',4,'%','d','e']
# list2=[3,'f',6,'d','e',3]
# list3=[12,3,12,15,14,15,17]
# list4=[12,42,41,12,41,12]
# tup = (2,42,41,12,41,12)
# list5=list(tup)
# sorted = sorted(list5)
# empty_list = []
# print(list5, sorted)
# =======================================================================

# COMMON ELEMENTS IN 2 LISTS  https://www.codespeedy.com/find-the-common-elements-in-two-lists-in-python/
# a=[2,3,4,5]
# b=[3,5,7,9]
# def common(a,b):
#     c = [value for value in a if value in b]
#     return c
# d=common(a,b)
# print(d)
# ***********************************************************
# def func(arr1, arr2):
#     return [x for x in arr1 if x in arr2]
# arr1 = [1, 2, 3]
# arr2 = [4, 3, 2, 1]
# print(func(arr1, arr2))
# # *************************************************************
# # #Defining function to check for common elements in two lists
# x=[2,3,4,5]
# y=[3,5,7,9]
# def commonelems(x,y):
#    common=0
#    for value in x:
#       if value in y:
#          common=1
#    if(not common):
#       return ("The lists have no common elements")
#    else:
#     return ("The lists have common elements")
# print(commonelems(x,y))

# #Checking two lists for common elements
# print("Comparing list1 and list2:")
# print(commonelems(x,y))
# print("\n")
# print("Comparing list1 and list3:")
# print(commonelems(list1,list3))
# print("\n")
# print("Comparing list3 and list4:")
# print(commonelems(list3,list4))
# https://www.tutorialspoint.com/python-check-if-two-lists-have-any-element-in-common
# =========================================================================================
"""
SUBARRAY SUM EQUAL K:
Given an unsorted array of integers, find the number of subarrays having a sum exactly equal to a given number k.
"""
# def count_all_subarrys(arr, n):
#     res = 0
#     for i in range(n):
#         summ = 0
#         for j in range(i, n):
#             summ += arr[j]
#             if summ == k:
#                 res += 1
#     return res
# arr = [10, 2, -2, -20, 10]
# n = len(arr)
# k = -10
# print(count_all_subarrys(arr, n))

# ===============================================================================
# # FIND THE DUPLICATES AND UNIQUES
# class Solution(object):
#    def findDuplicate(self, nums):
#        newlist = []  # empty list to hold unique elements from the list
#        duplist = []  # empty list to hold the duplicate elements from the list
#        for i in nums:
#            if i not in newlist:
#                newlist.append(i)
#            else:
#                duplist.append(i)  # this method catches the first duplicate entries, and appends them to the list
#
#        # The next step is to print the duplicate entries, and the unique entries
#        return "List of duplicates", duplist
#        # return "Unique Item List", newlist # prints the final list of unique items
# nums = [5, 3, 5, 2, 1, 6, 6, 4] # the original list of integers with duplicates
# ob1 = Solution()
# print(ob1.findDuplicate(nums))
# # ====================================================
#
# # UNIQUES AND DUPLICATES
# my_list = [2, 4, 44, 5, 2, 7, 5, 40]
# uniques = []
# duplicates = []
# for num in my_list:
#     if num not in uniques:
#         uniques.append(num)
# # print(uniques)
#     else:
#         duplicates.append(num)
# print(f"uniques: {uniques}")
# print(f"Duplicates:  {duplicates}")
# ====================================================================================

# LIST DIVIDE BY N
# l = [1,2,3,4,5,6]
# def divideByN(data, n):
#         return [data[i*n: (i+1)*n] for i in range(len(data)//n)]
# print(divideByN(l,2))
# [[1, 2], [3, 4], [5, 6]]
# print(divideByN(l,3))
# [[1, 2, 3], [4, 5, 6]]

# # GENERATORS VS ITERATORS
# def my_range(start, end):
#     current = start
#     while current < end:
#         yield current
#         current += 1
# nums = my_range(1,10)
# # GENERATORS TEST
# # print(next(nums))
# # print(next(nums))
# # print(next(nums))
# # print(next(nums))
# # print(next(nums))
# # ITERATORS TEST
# # for num in nums:
# #     print(num)
# ============================================================================================

# # CODE TO SWAP TWO NUMBERS
# p, q = 6, 5
# print(p, q)
# p, q = q, p
# print(p, q)
# =====================================================================

# # Longest substring without repeating characters
# class Solution:
#     def lenthOfLongestSubstring(self, s: str) -> int:
#         x = len(s)
#         unique_list = []
#         result = 0
#         for i in range(x):
#             for j in range(i, x):
#                 if (s[j] in unique_list):
#                     unique_list.clear()
#                     break
#                 else:
#                     unique_list.append(s[j])
#                     if (result < j - i + 1):
#                         result = j - i + 1
#             return result
# s = "abcabcbb"
# sol = Solution()
# result = sol.lenthOfLongestSubstring(s)
# print(result)
# ======================================================================

# # MEDIAN OF TWO SORTED ARRAYS
# class Solution(object):
#     def findMedianSortedArray(self, nums1, nums2):
#         nums = nums1 + nums2
#         nums.sort()
#         if len(nums) % 2 == 0:
#             return (nums[len(nums)//2] + nums[len(nums)//2 -1])/2.0
#         else:
#             return nums[len(nums)//2]
# nums1 = [1,2,5,]
# nums2 = [3,4,8,10]
# solution = Solution()
# result = solution.findMedianSortedArray(nums1,nums2)
# print(result)
# ====================================================================

# # CONTAINER WITH MOST WATER --- FINDING MAX AREA
# class Solution(object):
#     def maxArea(self, height):
#         low = 0
#         high = len(height) - 1
#         ans = 0
#         while low < high:
#             if height[low] < height[high]:
#                 min_height = height[low]
#                 min_height_index = low
#             else:
#                 min_height = height[high]
#                 min_height_index = high
#             ans = max((high - low) * min_height, ans)
#             if low + 1 == min_height_index + 1:
#                 low += 1
#             else:
#                 high -= 1
#         return ans
# obj1 = Solution()
# # result = obj1.maxArea([1,8,6,2,5,4,8,3,7])
# result = obj1.maxArea([2,1,5,6,2,3])
# print(result)
# ===================================================================

# # CONVERT INTEGER TO ROMAN FIGURES
# def solve(num):
#    res = ""
#    table = [
#       (1000, "M"),
#       (900, "CM"),
#       (500, "D"),
#       (400, "CD"),
#       (100, "C"),
#       (90, "XC"),
#       (50, "L"),
#       (40, "XL"),
#       (10, "X"),
#       (9, "IX"),
#       (5, "V"),
#       (4, "IV"),
#       (1, "I"),
#    ]
#    for cap, roman in table:
#       d, m = divmod(num, cap)
#       res += roman * d
#       num = m
#    return res
# num = 1999
# print(solve(num))
#
# # ============================================================
# # CONVERT ROMAN FIGURES TO INTEGERS
# def romanToInt(str):
#     total = 0
#     i = 0
#     values = {
#         "I": 1,
#         "V": 5,
#         "X": 10,
#         "L": 50,
#         "C": 100,
#         "D": 500,
#         "M": 1000,
#     }
#     while (i < len(str)):
#         s1 = values[str[i]]
#         if (i + 1 < len(str)):
#             s2 = values[str[i + 1]]
#             if (s1 >= s2):
#                 total = total + s1
#                 i = i + 1
#             else:
#                 total = total - s1
#                 i = i + 1
#         else:
#             total = total + s1
#             i = i + 1
#     return total
# print(romanToInt("MCMXCIX"))
# ===============================================================================

# # Finding all indices of a target item in a list
# def searchRange(search_list, target):
#     indices = []
#     for (index, item) in enumerate(search_list):
#         if item == target:
#             indices.append(index)
#     return indices
#     # else:
#     #     return None
# # a_list = [3, 6, 38, 6, 7, 38]
# # target = 38
# target = 'twitter'
# a_list = ['datagy', 'twitter', 'facebook', 'twitter', 'tiktok', 'youtube']
# print(searchRange(a_list, target))
# =======================================================================================

# class Solution(object):
#    def exist(self, board, word):
#       n =len(board)
#       m = len(board[0])
#       for i in range(n):
#          for j in range(m):
#             if word[0] == board[i][j]:
#                if self.find(board,word,i,j):
#                   return True
#       return False
#    def find(self, board,word,row,col,i=0):
#       if i == len(word):
#          return True
#       if row>= len(board) or row < 0 or col >= len(board[0]) or col<0 or word[i] != board[row][col]:
#          return False
#       board[row][col] = '*'
#       res = self.find(board,word,row+1,col,i+1) or self.find(board,word,row-1,col,i+1) or self.find(board,word,row,col+1,i+1) \
#             or self.find(board,word,row,col-1,i+1)
#       board[row][col] = word[i]
#       return res
# ob1 = Solution()
# print(ob1.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))
# ===============================================================================================

# LINEAR SEARCH
# # #Linear Search for target in data elements list
# data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
# target = 27
# def linear_search(data, target):
#     for i in range(len(data)):
#         if data[i] == target:
#             return f"True. Found at index {i}"
#     return "Not Found"
# x = linear_search(data, target)
# print(x)
# =============================================================================

# # Iterative Binary Search
# data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
# target = 17
# def bs_iter(data, target):
#     low = 0
#     high = len(data) - 1
#     while low <= high:
#         mid = (low+high) // 2
#         if target == data[mid]:
#             return True, data.index(target)
#         elif target < data[mid]: # if target in low half
#             high = mid - 1
#         else: # if target in high half
#             low = mid + 1
#     return False
# x = bs_iter(data, target)
# print(x)
# =======================================================================

# # Recursive Binary Search
# data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
# target = 33
# low = 0
# high = len(data) - 1
# def bs_recurs(data, target, low, high):
#     if low > high:
#         return "Not found"
#     else:
#         mid = (low + high) // 2
#         if target == data[mid]:
#             return f"Found at index {mid}"
#         elif target < data[mid]:
#             return bs_recurs(data, target, low, mid-1)
#         else:
#             return bs_recurs(data, target, mid+1, high)
# x = bs_recurs(data, target, low, high)
# print(x)
# ****************         ***************           *************

# # ITERATIVE BINARY ARRAY SEARCH
# def binary_itr(arr, start, end, target):
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] < target: # If target is on right side. Begin search from midway right-wards
#             start = mid + 1
#         elif arr[mid] > target: # If target is on left side. Begin search from midway left-wards
#             end = mid - 1
#         else:
#             return f"True. Found at index {arr.index(target)}" # If target matches mid. Return mid
#     return "Not found"
# arr = [2, 5, 8, 10, 16, 22, 25] # List is sorted
# target = 22
# result = binary_itr(arr, 0, len(arr) - 1, target)
# print(result)
# ========================================================================

# # BINARY SEARCH ARRAY
# def binary_search(list, target):
#     first = 0
#     last = len(list) - 1
#     while first <= last:
#         midpoint = (first + last) // 2
#         if list[midpoint] == target:
#             return midpoint
#         elif list[midpoint] < target: # search for target in list upper part
#             first = midpoint + 1
#         else:  # search for target in list lower part
#             last = midpoint - 1
#     return None
#
# def verify(index):
#     if index is not None:
#         print(f"Target found at index: {index}")
#     else:
#         print("target not found in list")
# numbers = [1,2,3,4,5,6,7,8,9,10]
# # numbers = [2,0,2,1,1,0]
# result = binary_search(numbers, 2)
# verify(result)
# ===================================================================

# def recursive_binary_search(list, target):
#     if len(list) == 0:
#         return False
#     else:
#         midpoint = (len(list)) // 2
#         if list[midpoint] == target:
#             return True
#         else:
#             if list[midpoint] < target:
#                 return recursive_binary_search(list[midpoint +1:], target)
#             else:
#                 return recursive_binary_search(list[:midpoint], target)
# def verify(result):
#     print(f"Target found: {result}")
# numbers = [1,2,3,4,5,6,7,8,9,10]
# result = recursive_binary_search(numbers, 6)
# verify(result)
# =========================================================================================
"""
NUMBER GUESSING GAME
Implement Binary Search Method
"""
# import random
# secret_number = random.randint(1, 50)
# while True:
#     guess = int(input("Guess the number between 1 and 50: "))
#     if guess == secret_number:
#         print("Congratulations! You got it!")
#         break
#     elif guess < secret_number:
#         print("Too low! Try again.")
#     else:
#         print("Too high! Try again.")
# ================================================================================================
# ARRAYS basically a python list
# =================================================

# # ARRAY SORT by Brute Force Method
# A = [-5, -23, 5, 0, 25, -6, 23, 67]
# # A = [2,0,2,1,1,0]
# C = []
# while A:
#     minimum =A[0]
#     for x in A:
#         if x < minimum:
#             minimum = x
#     C.append(minimum)
#     A.remove(minimum)
# print(C)
# ==============================================================================

# # BUBBLE SORT has efficiency based on iterations count
# def bubble_sort(A):
#     iters = 0
#     for i in range(len(A)):
#         # print(i)
#         for j in range(len(A)-i-1):
#             # print(j)
#             iters += 1
#             if A[j] > A[j+1]:
#                 A[j], A[j+1] = A[j+1], A[j]
#     return A, iters
# A = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(bubble_sort(A))
# ======================================================================================
"""
MERGE SORT:
Sorts a list in ascending order
Returns a new sorted list
Divide: Find the midpoint of the list and divide into sublists
Conquer: Recursively sort the sublists created in the previous step
Combine: Merge the sorted sublists created in the previous step
"""
# def merge_sort(values):
#     if len(values) <= 1:
#         return values
#     middle_index = len(values) // 2
#     left_values = merge_sort(values[:middle_index])
#     right_values = merge_sort(values[middle_index:])
#     print("%15s %-15s" % (left_values, right_values))
#     sorted_values = []
#     left_index = 0
#     right_index = 0
#     while left_index < len(left_values) and right_index < len(right_values):
#         if left_values[left_index] < right_values[right_index]:
#             sorted_values.append(left_values[left_index])
#             left_index += 1
#         else:
#             sorted_values.append(right_values[right_index])
#             right_index += 1
#     sorted_values += left_values[left_index:]
#     sorted_values += right_values[right_index:]
#     return sorted_values
# lst = [23,21,65,2,8,5]
# print(lst)
# sorted_nums = merge_sort(lst)
# print(sorted_nums)
# =====================================================================================
"""
#QUICK SORT: 
More efficient than other sort methods by computational cost
"""
# def quicksort(values):
#     if len(values) <= 1:
#         return values
#     less_than_pivot = []
#     greater_than_pivot = []
#     pivot = values[0]
#     for value in values[1:]:
#         if value <= pivot:
#             less_than_pivot.append(value)
#         else:
#             greater_than_pivot.append(value)
#     print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
#     return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
# # lst = [23,21,65,2,8,5]
# lst = [2,0,2,1,1,0]
# # print(lst)
# sorted_nums = quicksort(lst)
# print(sorted_nums)
# =====================================================================================

# SORTING ARRAYS BY INTERVALS
# def mergeIntervals(intervals):
#     # Sort the array on the basis of start values of intervals.
#     intervals.sort()
#     stack = []
#     # insert first interval into stack
#     stack.append(intervals[0])
#     for i in intervals[1:]:
#         # Check for overlapping interval,
#         # if interval overlap
#         if stack[-1][0] <= i[0] <= stack[-1][-1]:
#             stack[-1][-1] = max(stack[-1][-1], i[-1])
#         else:
#             stack.append(i)
#     return stack
#     # print("The Merged Intervals are :", end=" ")
#     # for i in range(len(stack)):
#     #     print(stack[i], end=" ")
# arr = [[6, 8], [1, 9], [2, 4], [4, 7]]
# print(mergeIntervals(arr))
# =====================================================================================
