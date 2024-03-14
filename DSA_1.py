# # ==========================================================================
# # REPEATED SUBSTRING PATTERN using Python
# def repeatedSubstringPattern(s):
#         string = (s + s)[1:-1] # a[1:-1] from the first to end item, reversed
#         return string.find(s) != -1 # find any existing, matching substring in the whole string
# print(repeatedSubstringPattern("abcabcabcabc"))
# ========================================================================

# # COUNTING BITS using Python
# def countBits(num):
#     counter = [0]
#     if num >= 1:
#         while len(counter) <= num:
#             counter = counter + [i + 1 for i in counter]
#         return counter[:num+1]
#     else:
#         return 0
# print(countBits(4))
# ============================================================================

# PERFECT SQUARE ----- validation using Python
# Given an integer, check if the integer is a perfect square.
# def isPerfectSquare(num):
#     left = 1
#     right = num
#     while left < right:
#         mid = (left + right) // 2
#         if mid * mid == num:
#             return True
#         elif mid * mid < num:
#             left = mid + 1
#         elif mid * mid > num:
#             right = mid
#     return False
# print(isPerfectSquare(49))
# ======================================================================

# FIRST UNIQUE CHARACTER ----- in a String
# def firstUniqueChar(s):
#     from collections import Counter
#     count = Counter(s)
#     for i, j in enumerate(s):
#         if count[j] == 1:
#             return f"First unique character is '{j}', at position index of '{i}'"
#     else:
#         return -1
# print(firstUniqueChar("ammannkkarwal"))
# ========================================================================
""""
# HAMMING DISTANCE BETWEEN TWO CHARACTERS -- is a measure of the difference between two strings of equal length.
# Given two integers, calculate the number of positions where the corresponding bits are different.
# For two integers: 1 and 4. The binary representation of 1 is 0001, and 4 is 0100.
# There are two positions where the corresponding bits of the integers are different. So the output is 2.
"""""
# def hammingDistance(x, y):
#     xor = x ^ y
#     dist = 0
#     while xor:
#         dist += 1
#         xor = xor & xor - 1
#     return dist
# x = 1
# y = 4
# print(hammingDistance(x, y))
# ===================================================================================

# MAX CONSECUTIVE ONES
# Find the maximum number of consecutive ones in a binary array.
# def findMaxConsecutiveOnes(nums):
#     max_count = 0
#     num_count = 0
#     for i in nums:
#         if i == 1:
#             num_count += 1
#         else:
#             max_count = max(max_count, num_count)
#             num_count = 0
#     return max(max_count, num_count)
#
# nums = [1,1,0,1,1,1,1]
# print(findMaxConsecutiveOnes(nums))
# ============================================================================================
"""
CONSTRUCT RECTANGLE
Return the dimensions of a rectangle with its given area such that its width and height
differ by the smallest possible number.
"""
# import math
# def constructRectangle(area):
#     w = int(math.sqrt(area))
#     while area % w != 0:
#         w -= 1
#     return [area // w, w]
# print(constructRectangle(30))
# =============================================================================================
"""
LICENSE TAGS FORMATTING
Given a license key, reformat the tag such that
each group contains the same length of characters except the first group.
"""
# def licenseTagFormatting(s, k):
#     s = s.upper().replace('-', '')
#     size = len(s)
#     s = s[::-1]
#     res = []
#     for i in range(0, size, k):
#         res.append(s[i:i+k])
#     return '-'.join(res)[::-1]
# print(licenseTagFormatting("2-4A0r7-4k", 3))
# ======================================================================================
"""
NUMBER OF SEGMENTS ... in a String
The output of the string in this example is 6 because there are six characters segments in the string.

The re.sub(” +”, ” “, s) uses the regular expression tool to remove extra white spaces in the string. 
Then we just need to use split to group into segments. The edge case is when the string is empty, 
which should return 0 segments instead.
"""
# importt re
# class Solution():
#     def countSegments(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         s = re.sub(" +", " ", s).strip()
#         return len(s.split(" ")) if s != '' else 0
# s = "Hello, my name is John"
# sol = Solution()
# result = sol.countSegments(s)
# print(result)
# """
# def countSegments(s):
#     count = len(s.split())
#     return count
# print(countSegments("Hey, my instagram username is amankharwal.official"))
# """
# =======================================================================================
"""
THIRD MAXIMUM NUMBER
Find the third maximum number in an array, given an array of integers.
"""
# def thirdMax(nums):
#     nums.sort(reverse = True)
#     count = 1
#     n = 0
#     previous = nums[0]
#     for i in range(len(nums)):
#         if nums[i] != previous:
#             count = count + 1
#             previous = nums[i]
#         if count == 3:
#             return nums[i]
#     return nums[0]
# nums = [10, 2, 4, 5, 6, 2, 9, 1, 7, 5, 4, 11, 30]
# print(thirdMax(nums))
# =========================================================================

# # Fizz Buzz
# def fizzBuzz(n):
#     output = []
#     for i in range(1, n + 1):
#         if (i % 3) == 0 and (i % 5) == 0:
#             output.append("FizzBuzz")
#         elif i % 3 == 0:
#             output.append("Fizz")
#         elif i % 5 == 0:
#             output.append("Buzz")
#         else:
#             output.append(str(i))
#     return output
# result = fizzBuzz(16)
# print(result)
# ==========================
# class Solution(object):
#     def fizzBuzz(self, n: int) -> list[str]:
#         output = []
#         for i in range(1, n + 1):
#             if (i % 3) == 0 and (i % 5) == 0:
#                 output.append("FizzBuzz")
#             elif i % 3 == 0:
#                 output.append("Fizz")
#             elif i % 5 == 0:
#                 output.append("Buzz")
#             else:
#                 output.append(str(i))
#         return output
# n = 16
# sol = Solution()
# result = sol.fizzBuzz(n)
# print(result)
# =============================================================================================

# # PRINTING STRINGS WITH FOR LOOP
# numbers = [2, 2, 2, 2, 10]
# numbers = [5, 2, 5, 2, 2]
# for str_ in numbers:
#     # print('X' * str_)
#     output = ''
#     for s in range(str_):
#         output += 'X'
#     print(output)
# ===============================================================================================
"""
POWER OF TWO
Given an integer. Return True if the integer is a power of two; otherwise, return False.
"""
# def isPowerOfTwo(n):
#     while (n != 1):
#         if (n % 2 != 0):
#             return False
#         n = n // 2
#     else:
#         return True
# print(isPowerOfTwo(60))
# ***************************
# Power of Three
# def isPowerOfThree(n):
#     while (n != 1):
#         if (n % 3 != 0):
#             return False
#         n = n // 3
#     else:
#         return True
# print(isPowerOfThree(81))
# =================================================================================================

# # MOVE ZEROS FORWARD
# def moveZeroes(nums):
#     zeroes = 0
#     for i in range(len(nums)):
#         if nums[i] > 0:
#             nums[zeroes], nums[i] = nums[i], nums[zeroes]
#             zeroes += 1
#     return nums
# nums = [0, 1, 0, 3, 12]
# print(moveZeroes(nums))
# ===================================================================================================
"""
UGLY NUMBER
If 2, 3, and 5 are the only prime factors of the input integer, then the integer is an ugly number,
and your output should return true
"""
# def isUgly(n):
#     if n > 0:
#         factors = [2, 3, 5]
#         for i in factors:
#             while n % i == 0:
#                 n = n // i
#         return n == 1
#     else:
#         return 0
# print(isUgly(16))
# ==============================================================================================
"""
ADD DIGITS OF A WHOLE NUMBERS
Given an integer of more than one digit. Add all the digits of the integer
till you get a single-digit value as the sum.
"""
# def addDigits(num):
#     while num > 9:
#         num = (num % 10) + (num // 10)
#     return num
# print(addDigits(1241))
# ==============================================================================================

# PATHS
# def paths(m, n):
#     row = [1] * n
#     print(row)
#     for i in range(m - 1):
#         newRow = [i] * n
#         for j in range(n-2, -1, -1):
#             newRow[j] = newRow[j+1] + row[j]
#         row = newRow
#         print(row)
#     return row[0]
# print(paths(3, 3))
# =================================================================================
"""
MAJORITY ELEMENT
Given an array nums of size n, return the majority element.
"""
# def majorityElement(arr):
#     # Size of the given array
#     n = len(arr)
#
#     for i in range(n):
#         # Selected element is arr[i]
#         cnt = 0
#         for j in range(n):
#             # Counting the frequency of arr[i]
#             if arr[j] == arr[i]:
#                 cnt += 1
#
#         # Check if frequency is greater than n/2
#         if cnt > (n // 2):
#             return arr[i]
#
#     return -1
#
# arr = [2, 2, 1, 1, 2, 2]
# ans = majorityElement(arr)
# print("The majority element is:", ans)

# ==================================================================================
"""
Pascal’s Triangle using Python
In the rows of a Pascal’s Triangle, each number is the sum of two numbers directly above it.
"""
# def generatePascal(numRows):
#     triangle = [[1]]
#     row = 0
#     while numRows > len(triangle):
#         row = row + 1
#         triangle.append([1] * (row + 1))
#         for i in range(1, row):
#             triangle[row][i] = triangle[row - 1][i - 1] + triangle[row -1][i]
#     return triangle
# print(generatePascal(6))
# print()
# ============================================================================================
"""
Excel Sheet Column Title using Python
Given an integer, return the corresponding column title of the integer as displayed in an excel sheet.
"""
# def convertToTitle(n):
#     title = ""
#     while n:
#         n = n - 1
#         title = chr(n % 26 + 65) + title
#         n = n // 26
#     return title
# print(convertToTitle(65))
# ============================================================================================
"""
SINGLE NUMBER PROBLEM
Given an array of integers where every item appears twice, find item that appears only once
"""
# def singleNumber(nums):
#     single = 0
#     for num in nums:
#         single = single ^ num
#     return single
# nums = [4, 1, 2, 1, 2, 4, 7]
# print(singleNumber(nums))
# ======================================================================================
"""
MAXIMUM PROFIT FINDER (Best Time to Buy and Sell Stock using Python)
Finding the best time to buy and sell a stock is also known as a maximum profit finder.
In the example below, the stock price is 7 on the first day. We bought the stock on day 2 at a price of 1 
and sold it on day 5 at a price of 6. Hence, maximum profit = 5 (6 – 1).
"""
# def maxProfit(prices):
#     buy = 0
#     sell = 1
#     max_profit = 0
#     while sell < len(prices):
#         if prices[sell] > prices[buy]:
#             profit = prices[sell] - prices[buy]
#             max_profit = max(profit, max_profit)
#         else:
#             buy = sell
#         sell = sell + 1
#     return max_profit
# prices = [7,1,5,3,6,4]
# print(maxProfit(prices))
# ========================================================================================
"""
CLIMBING STAIRS - FIBONACCI SEQUENCE METHOD
In the climbing stairs problem, you need to count the number of distinct ways to climb to the top of a staircase.
As it has a constraint, we can only climb one step or two steps at a time, so we have a choice of stepping on or
skipping a step. There are many ways to solve this problem. One of the simplest ways is to use the Fibonacci series method.
"""
# def climbStairs(num):
#     a = 1
#     b = 1
#     n = num - 1
#     for i in range(n):
#         c = a
#         a = a + b
#         b = c
#     return a
# print(climbStairs(10))
# *********************************
# def fib(num):
#     a, b = 0, 1
#     for i in range(0, num):
#         yield "{:2}: {}".format(i+1, a)
#         a, b = b, a + b
# for item in fib(10):
#     print(item)
# ================================================================================
"""
MISSING NUMBER
Given an array containing a range of numbers from 0 to n with a missing number,
find the missing number in the input array.
"""
# def findMissingNumbers(n):
#     numbers = n
#     output = []
#     for num in range(1, n[-1]):
#         if num not in numbers:
#             output.append(num)
#     return output
# listOfNumbers = [1, 3, 5, 6, 7, 8, 9, 10, 11, 13, 16]
# print(findMissingNumbers(listOfNumbers))
# =========================================================================================
"""
TWO SUM
For example, you are given an array [1, 2, 3, 4], and the target value is 3.
In this situation, the output should be 0,1 because the sum of 1 at index 0 and 2 at index 1 is equal to 3.
"""
# def twosum(nums, target):
#     length = len(nums)
#     for i in range(length):
#         for j in range(i + 1, length):
#             if nums[i] + nums[j] == target:
#                 return f"Indexes: {[i, j]} \nElements: {[nums[i], nums[j]]}"
# nums = [3, 4, 1, 7]
# target = 11
# print(twosum(nums, target))
# **********************************************
# def foursum(nums, target):
#     length = len(nums)
#     for i in range(length):
#         for j in range(i + 1, length):
#             for x in range(i + 1, length):
#                 for y in range(i + 1, length):
#                     if nums[i] + nums[j] + nums[x] + nums[y] == target:
#                         return [i, j, x, y]
# nums = [3, 4, 1, 7, 4, 9, 1]
# target = 9
# print(foursum(nums, target))
# ===========================================================================================
"""
SQUARE ROOT
A square root is a number that produces the specified value when multiplied by itself. 
For example, 5×5 gives 25, so the square root of 25 is 5.
"""
# def mySqrt(x):
#     left = 1
#     right = x
#     mid = 0
#     while (left <= right):
#         mid = (left + right) // 2
#         if mid * mid == x:
#             return mid
#         elif mid * mid > x:
#             right = mid - 1
#         else:
#             left = mid + 1
#             sqrt = mid
#     return sqrt
# print(mySqrt(37))


# Python 3 program to find floor(sqrt(x)

# Returns floor of square root of x


# def floorSqrt(x):
#
# 	# Base cases
# 	if (x == 0 or x == 1):
# 		return x
#
# 	# Do Binary Search for floor(sqrt(x))
# 	start = 1
# 	end = x//2
# 	while (start <= end):
# 		mid = (start + end) // 2
#
# 		# If x is a perfect square
# 		if (mid*mid == x):
# 			return mid
#
# 		# Since we need floor, we update
# 		# answer when mid*mid is smaller
# 		# than x, and move closer to sqrt(x)
# 		if (mid * mid < x):
# 			start = mid + 1
# 			ans = mid
#
# 		else:
#
# 			# If mid*mid is greater than x
# 			end = mid-1
#
# 	return ans
#
#
# # driver code
# x = 11
# print(floorSqrt(x))

# class Solution():
#     def mySqrt(self, x: int) -> int:
#         if x == 0:
#             return 0
#         last_guess = x / 2.0
#         while True:
#             guess = (last_guess + x / last_guess) / 2
#             if abs(guess - last_guess) < 0.000001:  # example threshold
#                 return int(guess)
#             last_guess = guess
#
# x = 43
# sol = Solution()
# result =  sol.mySqrt(x)
# print(result)

# ========================================================================================
"""
PLUS ONE
In the plus one problem, you will be given an array of digits, and you need to increment
the value of the last integer of the array by one to solve this problem. For example,
look at the input and output array mentioned below:
"""
# def plusOne(digits):
#     n = len(digits) - 1
#     while digits[n] == 9:
#         digits[n] = 0
#         n -= 1
#     if n < 0:
#         digits += [1]
#     else:
#         digits[n] += 1
#     return digits
# digits = [1, 2, 5, 7, 3, 6]
# print(plusOne(digits))
# =================================================================================
"""
REMOVE DUPLICATES
To remove duplicates from a sorted array, you need to create a new array by only storing the unique
values from the input array.
"""
# def removeDuplicate(items):
#     uniques = []
#     # duplicates = []
#     for num in items:
#         if num not in uniques:
#             uniques.append(num)
#             # return uniques
#         # else:
#             # duplicates.append(num)
#             # return duplicates
#     # return f"uniques: {uniques}\nDuplicates:  {duplicates}"
#     return f"Removed the duplicates leaving only uniques: {uniques}"
# my_list = [2, 4, 44, 5, 2, 7, 5, 40]
# print(removeDuplicate(my_list))
# ==========================================================================================
"""
MERGE TWO SORTED LISTS
To merge two sorted lists, combine two sorted lists in a way that the final
combined list is also in a sorted manner.
"""
# def merge2Lists(i, j):
#     mergedlist = []
#     while (i and j):
#         if (i[0] <= j[0]):
#             item = i.pop(0)
#             mergedlist.append(item)
#         else:
#             item = j.pop(0)
#             mergedlist.append(item)
#     mergedlist.extend(i if i else j)
#     return mergedlist
# list1 = [1, 3, 5, 7, 9, 12]
# list2 = [2, 4, 6, 8, 10, 11, 13]
# print(merge2Lists(list1, list2))
# ======================================================================================
"""
LONGEST COMMON PREFIX
To solve the Longest Common Prefix problem, you need to find the most common prefix in all the strings
of an array. For example, given an array of strings [“flower”, “flow”, “flog”], in this array,
the most common prefix among the first two items is “flo”
"""
# def longestCommonPrefix(strs):
#     l = len(strs[0])
#     for i in range(1, len(strs)):
#         length = min(l, len(strs[i]))
#         while length > 0 and strs[0][0:length] != strs[i][0:length]:
#             length -=  1
#             if length == 0:
#                 return 0
#     return strs[0][0:length]
#
# strs = ["flower", "flow", "flog"]
# print(longestCommonPrefix(strs))
# =========================================================================================
"""
GROUP ELEMENTS OF SAME INDEXES
To group elements of the same index, you will initially have two or more lists inside a list like
[[a, b], [c, d]]. To group the elements of these lists, you need to create two new lists to store
the elements of both the lists at index 0 [a, c] and index 1 [b, d]. That is the meaning of grouping
the elements of the same indices.
"""
# inputLists = [[10, 20, 30], [40, 50, 60], [71, 81, 91]]
# outputLists = []
# index = 0
# for i in range(len(inputLists[0])):
#     outputLists.append([])
#     for j in range(len(inputLists)):
#         outputLists[index].append(inputLists[j][index])
#     index += 1
# a, b, c = outputLists[0], outputLists[1], outputLists[2]
# print(f"{a} \n{b} \n{c}")

# =================================================================================

