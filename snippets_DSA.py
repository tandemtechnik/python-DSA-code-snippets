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

# NESTED LOOPS
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
#     # str1 = str1.replace("love", "enjoy").split()
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
#         print(char1)
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

# Calculate length of string
# input_str = "TandemTechniques"
# print(len(input_str))
# # Interative solution (Brute Force)
# def str_iter(input_str):
#     count = 0
#     for i in range(len(input_str)):
#         count += 1
#     return count
# x = str_iter(input_str)
# print(x)
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
# l2 = [2,1,3]
# sol = Solution()
# ans = sol.addnums(l1, l2)
# print(ans)
# =============================================================================

# Intersection of two lists
# A = [2, 3, 3, 5, 7, 11]
# B = [3, 3, 7, 15, 31]
# # print(set(A).intersection(B))
# def intersect(A, B):
#     i = 0
#     j = 0
#     intersection = []
#     while i < len(A) and j < len(B):
#         if A[i] == B[j]:
#             if i == 0 or A[i] != A[i-1]:
#                 intersection.append(A[i])
#             i += 1
#             j += 1
#         elif A[i] < B[j]:
#             i += 1
#         else: # A[i] > B[j]
#             j += 1
#     return intersection
# print(intersect(A, B))
# ================================================================================

# # STRINGS ... Find first occurrence of uppercase
# input_str_1 = "tandemTechniques"
# input_str_2 = "RandemTechniques"
# input_str_3 = "tandemtechniques"
#
# def find_upper_case(input_str):
#     for x in range(len(input_str)):
#         if input_str[x].isupper():
#             return input_str[x]
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
# # TWO SUM ----------- with for loop
# def two_sum(nums, target):
#     length = len(nums)
#     for i in range(length):
#         for j in range(i + 1, length):
#             if nums[i] + nums[j] == target:
#                 print(A[i], A[j]) # returns the numbers
#                 return [i, j]  # returns the numbers index
# nums = [-2, 3, 5, 4, 8, 9]
# target = 13
# print(two_sum(nums, target))
# =====================================================================================

# # CONSONANTS AND VOWELS counting IN A GIVEN STRING
# input_str_1 = "abc de"
# input_str_2 = "TandemtEcHniQEs"
# vowels = "aeiou"
# def consonants_count(input_str):
#     count = 0
#     for i in range(len(input_str)):
#         if input_str[i].lower() not in vowels and input_str[i].isalpha():
#             count += 1
#     return count
# print(consonants_count(input_str_1))
# print(consonants_count(input_str_2))
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
# # Function to add an item to stack . It
# # increases size by 1
# def push(stack, item):
#     stack.append(item)
#
# # Function to remove an item from stack.
# # It decreases size by 1
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
#     # Making the string empty since all
#     # characters are saved in stack
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
# ASSUME: Even number plus 1  results odd. Even plus even results even
# Find Binary reps of the int, then AND 1
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
# ===========================================================================================

# # SORTED ARRAY
# # # Find the index of first and last positions of target in a given sorted array
# arr = [2, 4, 5, 5, 5, 5, 5, 7, 9, 9]
# target = 5
# # output: [2, 6]
# def find_first_and_last(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             start = i
#             while i+1 < len(arr) and arr[i+1] == target:
#                 i += 1
#             return [start, i]
#     return [-1, -1]
# print(find_first_and_last(arr, target))
#
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
# print(find_start(arr, target))
#
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
# print(find_end(arr, target))
# =======================================================================================

# PAIRS OF PARENTHESIS
# """
# Given an integer n, generate all the valid combinations of n pairs of parenthesis
# input:
# n = 3
# output:
# ["((()))", "((()())", "(())()", "()(())", "()()()"]
# """
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

# LARGEST RECTANGLE
# """
# Find the largest rectangle in a given histogram
# """
# def largest_rectangle(heights):
#     heights = [-1]+heights+[-1]
#     max_area = 0
#     stack = [(0, 1)]
#     for i in range(1, len(heights)):
#         start = i
#         while stack[-1][1] > heights[i]:
#             top_index, top_height = stack.pop()
#             max_area = max(max_area, top_height*(i-top_index))
#             start = top_index
#         stack.append((start, heights[i]))
#     return max_area
# ============================================================================

# # UNIQUE PATHS
"""
Given two integers representing the size of a grid. using the size of the grid, the length, and breadth of the grid. 
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