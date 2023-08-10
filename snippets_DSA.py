"""
PALINDRUM
Function to check string is palindrome or not
"""
# def isPalindrome(str):
#         for i in range(0, int(len(str)/2)): # Run loop from 0 to len/2
#             if str[i] != str[len(str)-i-1]:
#                 return False
#             return True
# # s = "malayalam"
# s = "racecar"
# # s = "madam"
# ans = isPalindrome(s)
# if (ans):
#     print(f"Yes {s} is a palindrum")
# else:
#     print(f"No {s} isn't a palindrum")
# =======================
# string = input(("Enter a string:"))
# if(string == string[::-1]):
#       print("Word is a palindrome")
# else:
#       print("Word isn't a palindrome")
# ===========================
# num = int(input("Enter a number:"))
# temp = num
# rev = 0
# while(num > 0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if(temp==rev):
#     print("The number is palindrome!")
# else:
#     print("Not a palindrome!")
# =========================================================================

# # NESTED LOOPS
# n = 5
# m = 2
# for i in range(n):
#     print("Hey")
#     for j in range(m):
#         print("I love Python!")
# ============================================================================

# # FUNCTIONS
# def modify_str():
#     str1 = "I love Python"
#     str1.replace("love", "enjoy").split()
#     return str1
# print(modify_str())
# # ================================
# def modify_str():
#     str1 = "I love Python"
#     str1 = str1.replace("love", "enjoy").split()
#     return str1
# print(modify_str())
# =============================================================================

# MATCHING CHARACTERS
# Print matching characters in two strings
# string1 = "aabbcsdw"
# string2 = "abbbcsdd"
# for idx in range(len(string1)):
#     char1 = string1[idx]
#     char2 = string2[idx]
#     if char1 == char2:
#         print(char1, end=' ')
# ==================================================================================

# # Find Fixed Point in array of numbers
# A = [-10, -5, 0, 3, 7]
# def find_fxdp(A):
#     for i in range(len(A)):
#         if A[i] == i:
#             return A[i]
#     return None
# x = find_fxdp(A)
# print(x)
# =====================================================================================
"""
CALCULATE LENGTH OF A STRING
Interative solution (Brute Force)
"""
# def str_iter(input_str):
#     count = 0
#     for i in range(len(input_str)):
#         count += 1
#     return count
# input_str = "Tandem Techniques"
# x = str_iter(input_str)
# print(x)
# print(len(input_str))
# ============================================================================

# # ADD NUMBERS FROM TWO LISTS
# class Solution(object):
#     def addnums(self, l1, l2):
#         self.l1 = l1
#         self.l2 = l2
#         result = []
#         for i in range(len(l1)):
#             result.append(l1[i] + l2[i])
#         return result
# l1 = [3,3,3]
# l2 = [2,1,8]
# sol = Solution()
# ans = sol.addnums(l1, l2)
# print(ans)
#
# def addall(n):
#     sum = 0
#     for i in range(n):
#         sum += i
#     return sum
# numbers = int(input("Enter number: " )) # range(1,7) #[2, 5, 7, 12]
# result = addall(numbers)
# print(result)
# ================================================================================

# # STRINGS ... Find first occurrence of uppercase
# input_str_1 = "tandemTechniques"
# input_str_2 = "tandem Pechniques"
# input_str_3 = "tandemtechniques"
#
# def find_upper_case(input_str):
#     for x in range(len(input_str)):
#         if input_str[x].isupper():
#             return input_str[x], x
#     return "No uppercase found!"
# print(find_upper_case(input_str_1))
# print(find_upper_case(input_str_2))
# print(find_upper_case(input_str_3))
# ============================================================================================

# # STRING CONVERSION .. Convert numeric strings to integer without using int()
# def str_to_int(input_str):
#     output_int = 0
#     if input_str[0] == '-':
#         start_idx = 1
#         is_negative = True
#     else:
#         start_idx = 0
#         is_negative = False
#     for x in range(start_idx, len(input_str)):
#         place = 10**(len(input_str) - (x+1))
#         digit = ord(input_str[x]) - ord('0')
#         output_int += place * digit
#     if is_negative:
#         return -1 * output_int
#     else:
#         return output_int
# s = "123"
# print(str_to_int(s))
# s = "-123"
# print(str_to_int(s))
# ========================================================================================

# # TWO SUM  ----  with while loop
# A = [-2, 3, 5, 4, 8, 9]
# target = 13
# def two_sum(A, target):
#     i = 0
#     j = len(A) - 1
#     while i <= j:
#         if A[i] + A[j] == target:
#             print(A[i], A[j]) # returns the numbers
#             return [i, j] # returns the numbers index
#             #return True
#         elif A[i] + A[j] < target:
#             i += 1
#         else:
#             j -= 1
#     return False
# print(two_sum(A, target))
# #****************         *******************       ****************
# TWO SUM ----------- with for loop
# def two_sum(nums, target):
#     length = len(nums)
#     for i in range(length):
#         for j in range(i + 1, length):
#             if nums[i] + nums[j] == target:
#                 print(nums[i], nums[j]) # prints the numbers
#                 return [i, j]  # returns the numbers index
# nums = [-2, 3, 5, 4, 8, 9]
# target = 13
# print(two_sum(nums, target))
# =====================================================================================

# # CONSONANTS AND VOWELS COUNT IN A GIVEN STRING
# input_str_1 = "abcT de"
# # input_str_2 = "TandemtEcHniQEs"
# vowels = "aeiou"
# def consonants_count(input_str):
#     count = 0
#     for i in range(len(input_str)):
#         if input_str[i].lower() not in vowels and input_str[i].isalpha():
#             count += 1
#     return count
# print(consonants_count(input_str_1))
# # print(consonants_count(input_str_2))
# =====================================================================================

# # CODING CHALLENGE
# def func(lst):
#     for i in range(len(lst)):
#         lst[i] *= lst[i]
#     return lst
# lst = [2]
# func(lst) # calls the function again
# print(func(lst))
# =====================================================================================

# # PYTHON SEND EMAIL VIA GMAIL
# # pip install smtplib
# # vim sendemail.py
# import smtplib
# import config
#
# def sendemail(subject, msg):
#     try:
#         server = smtplib.SMTP('smtp.gmail.com:587')
#         server.ehlo()
#         server.starttls()
#         server.login(config.EMAIL_ADDRESS, config.PASSWORD)
#         message = 'Subject: {}\n\n{}'.format(subject, msg)
#         server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
#         server.quit()
#     except:
#         print("Email failed to send")
# subject = "Test subject"
# msg = "Hello there, hope you got my mail"
# sendemail(subject, msg)
# # python sendemail.py run from terminal
#
# # navigate to your gmail account and change settings: ALLOW LESS SECURE APPS: ON
# # https://myaccount.google.com/lesssecureapps
#
# # create config.py file in same folder
# # config.py
#
# # EMAIL_ADDRESS = ''
# # PASSWORD = ''
# ================================================================================================

# # REVERSE A STRING USING STACK
# # Function to create an empty stack. It
# # initializes size of stack as 0
# def createStack():
#     stack = []
#     return stack
#
# # Function to determine the size of the stack
# def size(stack):
#     return len(stack)
#
# # Stack is empty if the size is 0
# def isEmpty(stack):
#     if size(stack) == 0:
#         return True
#
# # Function to add an item to stack . It increases size by 1
# def push(stack, item):
#     stack.append(item)
#
# # Function to remove an item from stack. It decreases size by 1
# def pop(stack):
#     if isEmpty(stack):
#         return
#     return stack.pop()
#
# # A stack based function to reverse a string
# def reverse(string):
#     n = len(string)
#
#     # Create a empty stack
#     stack = createStack()
#
#     # Push all characters of string to stack
#     for i in range(0, n, 1):
#         push(stack, string[i])
#
#     # Making the string empty since all characters are saved in stack
#     string = ""
#
#     # Pop all characters of string and put them back to string
#     for i in range(0, n, 1):
#         string += pop(stack)
#     return string
# # Driver code
# s = "Geeksforgeeks"
# print("The original string is : ", end="")
# print(s)
# print("The reversed string(using stack) is : ", end="")
# print(reverse(s))
# ===================================================================================

# ODD or EVEN NUMBERS ----- determination
# Find Binary reps of the int, then AND 1
# ASSUME: Even number plus 1 results odd. Even plus even, results even
# def is_even_odd(x: int):
#     if x & 1 == 0:
#         return "Even"
#     return "Odd"
# print(is_even_odd(29))
# print(is_even_odd(10))
# ===================================================================================
"""
Return 2 sublists from list - "l" that have the same sum.
Return None if no such sublist exits.
"""
# def same_sum_sublists(l):
#     if l == 0:
#         return None
#     sum_l = sum(l)
#     if sum_l % 2 == 1:
#         # Odd, return early
#         return None
#     target_sum = sum_l / 2
#     runnin_sum = 0
#     for i in range(len(l)):
#         runnin_sum += l[i]
#         if runnin_sum == target_sum:
#             return l[:1 +1], l[i+1:]
#     return None
# print(same_sum_sublists([1, 2, 3]))
# print(same_sum_sublists([2, 3, 5]))
# print(same_sum_sublists([8, 5, 3]))
# =================================================================================
"""
Returns minimum time required to place mice in holes using Greedy approach.
"""
# def assignHole(mice, holes):
#     if len(mice) != len(holes): # mice and holes must be same length
#         return "Number of mice and hole not the same"
#     mice.sort()
#     holes.sort()
#     max_diff = 0
#     for i in range(len(mice)):
#         if max_diff < abs(mice[i] - holes[i]): # if the diff btw mice and holes > max_diff, then...
#             max_diff = abs(mice[i] - holes[i])
#         return max_diff
# mice = [4, -4, 2]
# holes = [4, 0, 5]
# min_tiime = assignHole(mice, holes)
# print(f"The last mouse gets into the hole in time: {min_tiime} mins")
# =========================================================================================
"""
UGLY NUMGER SEQUENCE by dynamic programming approach: If 2, 3, and 5 are the only prime factors 
of the input integer, then the integer is an ugly number.
"""
# def nth_Ugly(n):
#     dpUgly = [0] * n
#     dpUgly[0] = 1
#     u2 = u3 = u5 = 0
#     multiple_2 = 2
#     multiple_3 = 3
#     multiple_5 = 5
#     for i in range(1, n):
#         dpUgly[i] = min(multiple_2, multiple_3, multiple_5)
#         if dpUgly[i] == multiple_2:
#             u2 += 1
#             multiple_2 = dpUgly[u2] * 2
#         if dpUgly[i] == multiple_3:
#             u3 += 1
#             multiple_3 = dpUgly[u3] * 3
#         if dpUgly[i] == multiple_5:
#             u5 += 1
#             multiple_5 = dpUgly[u5] * 5
#     return dpUgly[n - 1]
# n = 15
# print(f"15th ugly number is: {nth_Ugly(n)}")
# ***************     *************   ****************
# def is_ugly(num):
#     if num == 0:
#         return False
#     for i in [2, 3, 5]:
#         while num % i == 0:
#             num /= i
#     return num == 1
# print(is_ugly(24))
# print(is_ugly(13))
# ********************************************************************************

# # INDEX OF FIRST AND LAST POSITION OF TARGET IN A SORTED ARRAY
# # Find the index of first and last positions of target in a given sorted array
# arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
# target = 5
# def find_first_and_last(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             start = i
#             while i+1 < len(arr) and arr[i+1] == target:
#                 i += 1
#             return [start, i]
#     return [-1, -1]
# print(find_first_and_last(arr, target))
# **********************************************
# BINARY SEARCH FOR ARRAY START
# def find_start(arr, target):
#     if arr[0] == target:
#         return 0
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target and arr[mid-1] < target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
# arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
# target = 5
# print(find_start(arr, target))
# **********************************************
# BINARY SEARCH FOR ARRAY END
# def find_end(arr, target):
#     if arr[-1] == target:
#         return len(arr) - 1
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target and arr[mid+1] > target:
#             return mid
#         elif arr[mid] > target:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return -1
# arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
# target = 5
# print(find_end(arr, target))
# =======================================================================================
"""
PAIRS OF PARENTHESIS
Given an integer n, generate all the valid combinations of n pairs of parenthesis
input:
n = 3
output:
["((()))", "((()())", "(())()", "()(())", "()()()"]
"""
# def is_valid(combination):
#     stack = []
#     for par in combination:
#         if par == "(":
#             stack.append(par)
#         else:
#             if len(stack) == 0:
#                 return False
#             else:
#                 stack.pop()
#     return len(stack) == 0
# combination = "()"
# print(is_valid(combination))
#*************       **********        **********
# def generate(n):
#     def rec(n, diff, comb, combs):
#         if diff < 0 or diff > n:
#             return
#         elif n == 0:
#             if diff == 0:
#                 combs.append(''.join(comb))
#         else:
#             comb.append('(')
#             rec(n-1, diff+1, comb, combs)
#             comb.pop()
#             comb.append(')')
#             rec(n-1, diff-1, comb, combs)
#             comb.pop()
#     combs = []
#     rec(2*n, 0, [], combs)
#     return combs
# n = 3
# print(generate(n))
# =============================================================================
"""
UNIQUE PATHS
Given two integers representing the size of a grid. using the size of the grid, the length, 
and breadth of the grid. 
Find the number of unique paths from the top left corner of the grid to the bottom right corner.
"""
# class Solution(object):
#    def uniquePaths(self, m, n):
#       row = n
#       column = m
#       dp = [[-1 for i in range(m)] for j in range(n)]
#       dp[row-2][column-1] = 1
#       for i in range(column):
#          dp[n-1][i] = 1
#       for i in range(row):
#          dp[i][column-1]=1
#       for i in range(row-2,-1,-1):
#          for j in range(column-2,-1,-1):
#             dp[i][j] = dp[i+1][j] + dp[i][j+1]
#       return dp[0][0]
# ob1 = Solution()
# print(ob1.uniquePaths(3, 7))
# ================================================================================
"""
DAILY TEMPERATURES:
Suppose we have a list of daily temperatures T, we have to return a list such that, for each day in the input, 
shows how many days we would have to wait until a warmer temperature. If there is no future day for which this is possible, 
store 0 instead. For example, if T = [73, 74, 75, 71, 69, 72, 76, 73], output will be [1, 1, 4, 2, 1, 1, 0, 0].
"""
# class Solution(object):
#    def dailyTemperatures(self, T):
#       ans = [0 for i in range(len(T))]
#       stack = []
#       stack.append(0)
#       i=1
#       while i <len(T):
#          while len(stack) and T[i]>T[stack[-1]]:
#             index = stack[-1]
#             ans[index] = i-index
#             stack.pop()
#          if not len(stack) or T[i]<=T[stack[-1]]:
#             stack.append(i)
#          i+=1
#       return ans
# ob1 = Solution()
# print(ob1.dailyTemperatures([73,74,75,71,69,72,76,73]))
# ================================================================================

# # STOCK BUY AND SELL
# S = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
# # S = [7,1,5,3,6,4]
# def bs_Stock(S):
#     max_profit = 0
#     for i in range(len(S)):
#         for j in range(i+1, len(S)):
#             if S[j] - S[i] > max_profit:
#                 max_profit = S[j] - S[i]
#     return max_profit
# result = bs_Stock(S)
# print(result)
# ===================================================================================

# # LOOP THROUGH ARRAYS
# nums = [1, 2, 3]
#
# # Using Index
# for i in range(len(nums)):
#     print(i, nums[i])
#
# # Without Index
# for n in nums:
#     print(n)
#
# # With index and Value
# for i, n in enumerate(nums):
#     print(i, n)
# ************************************

# SORTING BY SECOND LETTER
# z = ('Kelvin', 'Niklaus', 'Jenny', 'Craig')
# print(sorted(z))
# print(sorted(z, key=lambda K: K[1]))
# *********************************************
# SQUARED NUMBER FUNCTION
# def get_squared_numbers(numbers):
#     squared_numbers = []
#     for n in numbers:
#         squared_numbers.append(n*n)
#     return squared_numbers
#
# numbers = [2, 5, 8, 9]
# print(get_squared_numbers(numbers))
# # ******************************************

# # DUPLICATES
# numbers = [3, 6, 2, 4, 3, 6, 8, 9]
#
# for i in range(len(numbers)):
#     for j in range(i+1, len(numbers)):
#         # print(numbers[i], numbers[j])
#         if numbers[i] == numbers[j]:
#             print(f"{numbers[i]} ia a duplicate")
#             # break
# ***********************************
# # Python program to print duplicates from a list of integers
# def Repeat(x):
#     _size = len(x)
#     duplicates = []
#     for i in range(_size):
#         k = i + 1
#         for j in range(k, _size):
#             if x[i] == x[j] and x[i] not in duplicates:
#                 duplicates.append(x[i])
#     return duplicates
#
# list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# print(Repeat(list1))
# *******************************************************

# STRING SLICING
# heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
# heros[1:4] = ['doctor strange']
# print(heros)
# # ***************************************

# ODD NUMBERS FROM N
# number = int(input("Pls enter any number: "))
# odd_nums = []
# odd_total = 0
# for num in range(1, number):
#     # print(num)
#     if num % 2 == 1:
#         odd_nums.append(num)
#         odd_total += num
# print(f"{odd_nums} \n{odd_total}")
# # *******************************************

# FIND AVERAGE OF NUMBERS
# Python code to get average of list
# def Average(lst):
#     sum_of_list = 0
#     # for i in range(len(lst)):
#     for nums in lst:
#         # sum_of_list += lst[i]
#         sum_of_list += nums
#         average = sum_of_list/len(lst)
#     return average

# lst = [15, 9, 55, 41, 35, 20, 62, 49]
# avrg = Average(lst)
# print(f"Average of the list = {round(avrg, 2)}")
# ***********************

# def calculate_average(values):
#     if type(values) is not str:
#         if "__iter__" in dir(values):
#             sum_expr = "+".join(str(v) for v in values)
#             avg_expr = f"({sum_expr}) / {len(values)}"
#             average = eval(avg_expr)
#             return average
#         else:
#             return None
#     return values
# # items = "[12, 34, 56, 78]"
# items = [12, 34, 56, 78]
# result = calculate_average(items)
# print(result)
# ********************************************************

# REMOVE ELEMENT FROM LIST
# class Solution(object):
#     def removeElement(self, nums, val):
#
#         if val == []:
#             return 0
#         else:
#             i = 0
#             j = 0
#             while j < len(nums):
#                 if nums[j] == val:
#                     j += 1
#                 else:
#                     nums[i] = nums[j]
#                     i += 1
#                     j += 1
#         return len(nums[0:i])
# nums = [3,2,2,3]
# val = 3
# soln = Solution()
# result = soln.removeElement(nums, val)
# print(result)
# *********************************************************************
"""
REVERSE STRING
Write a function that takes a string as input and returns the string reversed. 
Example: Given s = "hello", return "olleh".
"""
# class Solution(object):
#     def reverseString(self, s):
#         current_str = [char for char in s]
#         i=0
#         j = len(s) - 1
#         while i < j:
#             temp = current_str[i]
#             current_str[i] = current_str[j]
#             current_str[j] = temp
#             j -= 1
#             i += 1
#         return "".join(current_str)
#
# s = "TANDEM TECHNIQUES"
# soln = Solution()
# result = soln.reverseString(s)
# print(result)
# ***********************************************************
"""
MERGE SORTED ARRAYS
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
Note: You may assume that nums1 has enough space (size that is greater or equal to m + n) 
to hold additional elements from nums2. 
The number of elements initialized in nums1 and nums2 are m and n respectively.
"""
# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         last1 = m - 1
#         last2 = n - 1
#         last = m + n - 1
#         while last1 >= 0 and last2 >= 0:
#             if nums1[last1] > nums2[last2]:
#                 nums1[last] = nums1[last1]
#                 last1 -= 1
#                 last -= 1
#             else:
#                 nums1[last] = nums2[last2]
#                 last2 -= 1
#                 last -= 1
#         while last2 >= 0:
#             nums1[last] = nums2[last2]
#             last -= 1
#             last2 -= 1
# ************************************************************
# # REVERSE LINKED LIST
# class Solution(object):
#     def reverseList(self, head):
#         if head == None:
#             return None
#         elif head != None and head.next == None:
#             return head
#         else:
#             temp = None
#             next_node = None
#             while head != None:
#                 next_node = head.next
#                 head.next = temp
#                 temp = head
#                 head = next_node
#             return temp
# *********************************************************************
"""
DELETE NODE IN A LINKED LIST
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value 3, 
the linked list should become 1 -> 2 -> 4 after calling your function.
"""
# def __init__(self, x):
#     self.val = x
#     self.next = None
# class Solution(object):
#     def deleteNode(self, node):
#
#         if node == None:
#             pass
#         else:
#             next_node = node.next
#             node.val = next_node.val
#             node.next = next_node.next
# ***********************************************************************
"""
PAINT FENCE
There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence. Note: n and k are non-negative integers.
"""
# class Solution(object):
#     def numWays(self, n, k):
#         dp = [0, k, k*k, 0]
#         if n <= 2:
#             return dp[n]
#         for i in range(2, n):
#             dp[3] = (k-1)*(dp[1] + dp[2])
#             dp[1] = dp[2]
#             dp[2] = dp[3]
#         return dp[3]
# ************************************************************
"""
BULB SWITCHER
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. 
On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). 
For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb. 
Find how many bulbs are on after n rounds.
Example: Given n = 3.
At first, the three bulbs are [off, off, off]. After first round, the three bulbs are [on, on, on]. 
After second round, the three bulbs are [on, off, on]. After third round, the three bulbs are [on, off, off].
So you should return 1, because there is only one bulb is on.
"""
# import math
# class Solution(object):
#     def bulbSwitch(self, n):
#         return int(math.sqrt(n))
# ***********************************************************************

# # SEARCH INSERT POSITION
# class Solution:
#   def searchInsert(self, nums: list[int], target: int) -> int:
#     l = 0
#     r = len(nums)
#
#     while l < r:
#       m = (l + r) // 2
#       if nums[m] == target:
#         return m
#       if nums[m] < target:
#         l = m + 1
#       else:
#         r = m
#
#     return l
# *********************************************************************
