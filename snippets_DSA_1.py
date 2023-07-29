# # Linked List
# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def print(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
#             itr = itr.next
#         print(llstr)
#
#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count+=1
#             itr = itr.next
#
#         return count
#
#     def insert_at_begining(self, data):
#         node = Node(data, self.head)
#         self.head = node
#
#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return
#
#         itr = self.head
#
#         while itr.next:
#             itr = itr.next
#
#         itr.next = Node(data, None)
#
#     def insert_at(self, index, data):
#         if index<0 or index>self.get_length():
#             raise Exception("Invalid Index")
#
#         if index==0:
#             self.insert_at_begining(data)
#             return
#
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr.next)
#                 itr.next = node
#                 break
#
#             itr = itr.next
#             count += 1
#
#     def remove_at(self, index):
#         if index<0 or index>=self.get_length():
#             raise Exception("Invalid Index")
#
#         if index==0:
#             self.head = self.head.next
#             return
#
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 break
#
#             itr = itr.next
#             count+=1
#
#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)
#
#
# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.insert_at(1,"blueberry")
#     ll.remove_at(2)
#     ll.print()
#
#     ll.insert_values([45,7,12,567,99])
#     ll.insert_at_end(67)
#     ll.print()
# ************************************************************************
"""
Exercise: Linked List
In LinkedList class that we implemented in our tutorial add following two methods,
def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node

def remove_by_value(self, data):
    # Remove first node that contains data
Now make following calls,

    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
"""
# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def print(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data) + ' --> '
#             itr = itr.next
#         print(llstr)
#
#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count+=1
#             itr = itr.next
#
#         return count
#
#     def insert_at_begining(self, data):
#         node = Node(data, self.head)
#         self.head = node
#
#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return
#
#         itr = self.head
#
#         while itr.next:
#             itr = itr.next
#
#         itr.next = Node(data, None)
#
#     def insert_at(self, index, data):
#         if index<0 or index>self.get_length():
#             raise Exception("Invalid Index")
#
#         if index==0:
#             self.insert_at_begining(data)
#             return
#
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr.next)
#                 itr.next = node
#                 break
#
#             itr = itr.next
#             count += 1
#
#     def remove_at(self, index):
#         if index<0 or index>=self.get_length():
#             raise Exception("Invalid Index")
#
#         if index==0:
#             self.head = self.head.next
#             return
#
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 break
#
#             itr = itr.next
#             count+=1
#
#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)
#
#
#     def insert_after_value(self, data_after, data_to_insert):
#         if self.head is None:
#             return
#
#         if self.head.data==data_after:
#             self.head.next = Node(data_to_insert,self.head.next)
#             return
#
#         itr = self.head
#         while itr:
#             if itr.data == data_after:
#                 itr.next = Node(data_to_insert, itr.next)
#                 break
#
#             itr = itr.next
#
#     def remove_by_value(self, data):
#         if self.head is None:
#             return
#
#         if self.head.data == data:
#             self.head = self.head.next
#             return
#
#         itr = self.head
#         while itr.next:
#             if itr.next.data == data:
#                 itr.next = itr.next.next
#                 break
#             itr = itr.next
#
# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.print()
#     ll.insert_after_value("mango","apple")
#     ll.print()
#     ll.remove_by_value("orange")
#     ll.print()
#     ll.remove_by_value("figs")
#     ll.print()
#     ll.remove_by_value("banana")
#     ll.remove_by_value("mango")
#     ll.remove_by_value("apple")
#     ll.remove_by_value("grapes")
#     ll.print()
#
#     # ll.insert_values([45,7,12,567,99])
#     # ll.insert_at_end(67)
#     # ll.print()
# # ************************************************************
"""
Exercise: Linked List
In LinkedList class that we implemented in our tutorial add following two methods,
def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurrence of data_after value in linked list
    # Now insert data_to_insert after data_after node

def remove_by_value(self, data):
    # Remove first node that contains data
Now make following calls,

    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
"""
# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def print(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data) + ' --> '
#             itr = itr.next
#         print(llstr)
#
#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count+=1
#             itr = itr.next
#
#         return count
#
#     def insert_at_begining(self, data):
#         node = Node(data, self.head)
#         self.head = node
#
#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None)
#             return
#
#         itr = self.head
#
#         while itr.next:
#             itr = itr.next
#
#         itr.next = Node(data, None)
#
#     def insert_at(self, index, data):
#         if index<0 or index>self.get_length():
#             raise Exception("Invalid Index")
#
#         if index==0:
#             self.insert_at_begining(data)
#             return
#
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr.next)
#                 itr.next = node
#                 break
#
#             itr = itr.next
#             count += 1
#
#     def remove_at(self, index):
#         if index<0 or index>=self.get_length():
#             raise Exception("Invalid Index")
#
#         if index==0:
#             self.head = self.head.next
#             return
#
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 itr.next = itr.next.next
#                 break
#
#             itr = itr.next
#             count+=1
#
#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)
#
#
#     def insert_after_value(self, data_after, data_to_insert):
#         if self.head is None:
#             return
#
#         if self.head.data==data_after:
#             self.head.next = Node(data_to_insert,self.head.next)
#             return
#
#         itr = self.head
#         while itr:
#             if itr.data == data_after:
#                 itr.next = Node(data_to_insert, itr.next)
#                 break
#
#             itr = itr.next
#
#     def remove_by_value(self, data):
#         if self.head is None:
#             return
#
#         if self.head.data == data:
#             self.head = self.head.next
#             return
#
#         itr = self.head
#         while itr.next:
#             if itr.next.data == data:
#                 itr.next = itr.next.next
#                 break
#             itr = itr.next
#
# if __name__ == '__main__':
#     ll = LinkedList()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.print()
#     ll.insert_after_value("mango","apple")
#     ll.print()
#     ll.remove_by_value("orange")
#     ll.print()
#     ll.remove_by_value("figs")
#     ll.print()
#     ll.remove_by_value("banana")
#     ll.remove_by_value("mango")
#     ll.remove_by_value("apple")
#     ll.remove_by_value("grapes")
#     ll.print()
#
#     # ll.insert_values([45,7,12,567,99])
#     # ll.insert_at_end(67)
#     # ll.print()
# # **************************************************************************
"""
Implement doubly linked list. The only difference with regular linked list is that double linked has prev 
node reference as well. That way you can iterate in forward and backward direction. Your node class will 
look this this,
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
Add following new methods,

def print_forward(self):
    # This method prints list in forward direction. Use node.next

def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
Implement all other methods in regular linked list c
lass and make necessary changes for doubly linked list (you need to populate node.prev in all those methods)
"""
# class Node:
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#
#     def print_forward(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#
#         itr = self.head
#         llstr = ''
#         while itr:
#             llstr += str(itr.data) + ' --> '
#             itr = itr.next
#         print(llstr)
#
#     def print_backward(self):
#         if self.head is None:
#             print("Linked list is empty")
#             return
#
#         last_node = self.get_last_node()
#         itr = last_node
#         llstr = ''
#         while itr:
#             llstr += itr.data + '-->'
#             itr = itr.prev
#         print("Link list in reverse: ", llstr)
#
#     def get_last_node(self):
#         itr = self.head
#         while itr.next:
#             itr = itr.next
#
#         return itr
#
#     def get_length(self):
#         count = 0
#         itr = self.head
#         while itr:
#             count+=1
#             itr = itr.next
#
#         return count
#
#     def insert_at_begining(self, data):
#         if self.head == None:
#             node = Node(data, self.head, None)
#             self.head = node
#         else:
#             node = Node(data, self.head, None)
#             self.head.prev = node
#             self.head = node
#
#     def insert_at_end(self, data):
#         if self.head is None:
#             self.head = Node(data, None, None)
#             return
#
#         itr = self.head
#
#         while itr.next:
#             itr = itr.next
#
#         itr.next = Node(data, None, itr)
#
#     def insert_at(self, index, data):
#         if index<0 or index>self.get_length():
#             raise Exception("Invalid Index")
#
#         if index==0:
#             self.insert_at_begining(data)
#             return
#
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index - 1:
#                 node = Node(data, itr.next, itr)
#                 if node.next:
#                     node.next.prev = node
#                 itr.next = node
#                 break
#
#             itr = itr.next
#             count += 1
#
#     def remove_at(self, index):
#         if index<0 or index>=self.get_length():
#             raise Exception("Invalid Index")
#
#         if index==0:
#             self.head = self.head.next
#             self.head.prev = None
#             return
#
#         count = 0
#         itr = self.head
#         while itr:
#             if count == index:
#                 itr.prev.next = itr.next
#                 if itr.next:
#                     itr.next.prev = itr.prev
#                 break
#
#             itr = itr.next
#             count+=1
#
#     def insert_values(self, data_list):
#         self.head = None
#         for data in data_list:
#             self.insert_at_end(data)
#
#
# if __name__ == '__main__':
#     ll = DoublyLinkedList()
#     ll.insert_values(["banana","mango","grapes","orange"])
#     ll.print_forward()
#     ll.print_backward()
#     ll.insert_at_end("figs")
#     ll.print_forward()
#     ll.insert_at(0,"jackfruit")
#     ll.print_forward()
#     ll.insert_at(6,"dates")
#     ll.print_forward()
#     ll.insert_at(2,"kiwi")
#     ll.print_forward()
# ***************************************************************************
#
# def my_family(age):
#
#     family = {
#         'dad': range(40, 100),
#         'mom': range(50),
#         'child': range(0, 18)
#     }
#     for member, age_range in family.items():
#         if age in age_range:
#             return member
#     return "Unknown"
# print(my_family(145))
# # **********************************
# def my_family(age):
#
#     family = {
#         'dad': range(40, 100),
#         'mom': range(50),
#         'child': range(0, 18)
#     }
#     members = []
#     for member, age_range in family.items():
#         if age in age_range:
#             members.append(member)
#     return members
# print(my_family(45))
# **************************************************
#
# """
# Exercise: Hash Table: New York City Weather Analysis
# (1) nyc_weather.csv contains new york city weather for first few days in the month of January.
# Write a program that can answer following,
#
#   (a) What was the average temperature in first week of Jan
#
#   (b) What was the maximum temperature in first 10 days of Jan
#
#   Figure out data structure that is best for this problem
#   """
#
# arr = []
#
# with open("nyc_weather.csv","r") as f:
#     for line in f:
#         tokens = line.split(',')
#         try:
#             temperature = int(tokens[1])
#             arr.append(temperature)
#         except:
#             print("Invalid temperature.Ignore the row")
# # Invalid temperature.Ignore the row
# arr
# [27, 31, 23, 34, 37, 38, 29, 30, 35, 30]
#
# # What was the average temperature in first week of Jan
# sum(arr[0:7])/len(arr[0:7])
# 31.285714285714285
#
# # What was the maximum temperature in first 10 days of Jan
# arr[0:10]
# [27, 31, 23, 34, 37, 38, 29, 30, 35, 30]
# max(arr[0:10])
# 38
#
# """
# The best data structure to use here was a list because all we wanted was access of temperature elements
# (2) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program
# that can answer following,
#
#   (a) What was the temperature on Jan 9?
#
#   (b) What was the temperature on Jan 4?
#
#   Figure out data structure that is best for this problem
# """
# weather_dict = {}
#
# with open("nyc_weather.csv","r") as f:
#     for line in f:
#         tokens = line.split(',')
#         day = tokens[0]
#         try:
#             temperature = int(tokens[1])
#             weather_dict[day] = temperature
#         except:
#             print("Invalid temperature.Ignore the row")
# # Invalid temperature.Ignore the row
# weather_dict
# {'Jan 1': 27,
#  'Jan 2': 31,
#  'Jan 3': 23,
#  'Jan 4': 34,
#  'Jan 5': 37,
#  'Jan 6': 38,
#  'Jan 7': 29,
#  'Jan 8': 30,
#  'Jan 9': 35,
#  'Jan 10': 30}
#
# # What was the temperature on Jan 9
# weather_dict['Jan 9']
# 35
#
# # What was the temperature on Jan 4
# weather_dict['Jan 4']
# 34
#
# """
# The best data structure to use here was a dictionary (internally a hash table) because we wanted to know temperature for
# specific day, requiring key, value pair access where you can look up an element by day using O(1)
# complexity
# """
# # **************************************************************************
# """
# Exercise: Hash Table: New York City Weather Analysis
# (1) nyc_weather.csv contains new york city weather for first few days in the month of January.
# Write a program that can answer following,
#
#   (a) What was the average temperature in first week of Jan
#
#   (b) What was the maximum temperature in first 10 days of Jan
#
#   Figure out data structure that is best for this problem
# """
# arr = []
#
# with open("nyc_weather.csv","r") as f:
#     for line in f:
#         tokens = line.split(',')
#         try:
#             temperature = int(tokens[1])
#             arr.append(temperature)
#         except:
#             print("Invalid temperature.Ignore the row")
# # Invalid temperature.Ignore the row
# arr
# [27, 31, 23, 34, 37, 38, 29, 30, 35, 30]
#
# # What was the average temperature in first week of Jan
# sum(arr[0:7])/len(arr[0:7])
# 31.285714285714285
#
# # What was the maximum temperature in first 10 days of Jan
# arr[0:10]
# [27, 31, 23, 34, 37, 38, 29, 30, 35, 30]
# max(arr[0:10])
# 38
#
# """
# The best data structure to use here was a list because all we wanted was access of temperature elements
# (2) nyc_weather.csv contains new york city weather for first few days in the month of January.
# Write a program that can answer following,
#
#   (a) What was the temperature on Jan 9?
#
#   (b) What was the temperature on Jan 4?
#
#   Figure out data structure that is best for this problem
# """
# weather_dict = {}
#
# with open("nyc_weather.csv","r") as f:
#     for line in f:
#         tokens = line.split(',')
#         day = tokens[0]
#         try:
#             temperature = int(tokens[1])
#             weather_dict[day] = temperature
#         except:
#             print("Invalid temperature.Ignore the row")
# # Invalid temperature.Ignore the row
# weather_dict
# {'Jan 1': 27,
#  'Jan 2': 31,
#  'Jan 3': 23,
#  'Jan 4': 34,
#  'Jan 5': 37,
#  'Jan 6': 38,
#  'Jan 7': 29,
#  'Jan 8': 30,
#  'Jan 9': 35,
#  'Jan 10': 30}
#
# # What was the temperature on Jan 9
# weather_dict['Jan 9']
# 35
#
# # What was the temperature on Jan 4
# weather_dict['Jan 4']
# 34
# """
# The best data structure to use here was a dictionary (internally a hash table) because we wanted to know
# temperature for specific day, requiring key, value pair access where you can look up an element by day
# using O(1) complexity
# """
# # ************************************************************
# """
# FIND WORD OCCURRENCES IN A FILE
# poem.txt Contains famous poem "Road not taken" by poet Robert Frost.
# You have to read this file in python and print every word and its count as show below.
# Think about the best data structure that you can use to solve this problem and figure out
# why you selected that specific data structure.
#  'diverged': 2,
#  'in': 3,
#  'I': 8
# """
# with open("poem.txt","r") as f:
#     for line in f:
#         print(line)
# """
# Two roads diverged in a yellow wood,
#
# And sorry I could not travel both
#
# And be one traveler, long I stood
#
# And looked down one as far as I could
#
# To where it bent in the undergrowth;
#
#
#
# Then took the other, as just as fair,
#
# And having perhaps the better claim,
#
# Because it was grassy and wanted wear;
#
# Though as for that the passing there
#
# Had worn them really about the same,
#
#
#
# And both that morning equally lay
#
# In leaves no step had trodden black.
#
# Oh, I kept the first for another day!
#
# Yet knowing how way leads on to way,
#
# I doubted if I should ever come back.
#
#
#
# I shall be telling this with a sigh
#
# Somewhere ages and ages hence:
#
# Two roads diverged in a wood, and Iâ€”
#
# I took the one less traveled by,
#
# And that has made all the difference.
# """
#
# word_count = {}
# with open("poem.txt","r") as f:
#     for line in f:
#         tokens = line.split(' ')
#         for token in tokens:
#             token=token.replace('\n','')
#             if token in word_count:
#                 word_count[token]+=1
#             else:
#                 word_count[token]=1
# print(word_count)
# """
# {'Two': 2,
#  'roads': 2,
#  'diverged': 2,
#  'in': 3,
#  'a': 3,
#  'yellow': 1,
#  'wood,': 2,
#  'And': 6,
#  'sorry': 1,
#  'I': 8,
#  'could': 2,
#  'not': 1,
#  'travel': 1,
#  'both': 2,
#  'be': 2,
#  'one': 3,
#  'traveler,': 1,
#  'long': 1,
#  'stood': 1,
#  'looked': 1,
#  'down': 1,
#  'as': 5,
#  'far': 1,
#  'To': 1,
#  'where': 1,
#  'it': 2,
#  'bent': 1,
#  'the': 8,
#  'undergrowth;': 1,
#  '': 3,
#  'Then': 1,
#  'took': 2,
#  'other,': 1,
#  'just': 1,
#  'fair,': 1,
#  'having': 1,
#  'perhaps': 1,
#  'better': 1,
#  'claim,': 1,
#  'Because': 1,
#  'was': 1,
#  'grassy': 1,
#  'and': 3,
#  'wanted': 1,
#  'wear;': 1,
#  'Though': 1,
#  'for': 2,
#  'that': 3,
#  'passing': 1,
#  'there': 1,
#  'Had': 1,
#  'worn': 1,
#  'them': 1,
#  'really': 1,
#  'about': 1,
#  'same,': 1,
#  'morning': 1,
#  'equally': 1,
#  'lay': 1,
#  'In': 1,
#  'leaves': 1,
#  'no': 1,
#  'step': 1,
#  'had': 1,
#  'trodden': 1,
#  'black.': 1,
#  'Oh,': 1,
#  'kept': 1,
#  'first': 1,
#  'another': 1,
#  'day!': 1,
#  'Yet': 1,
#  'knowing': 1,
#  'how': 1,
#  'way': 1,
#  'leads': 1,
#  'on': 1,
#  'to': 1,
#  'way,': 1,
#  'doubted': 1,
#  'if': 1,
#  'should': 1,
#  'ever': 1,
#  'come': 1,
#  'back.': 1,
#  'shall': 1,
#  'telling': 1,
#  'this': 1,
#  'with': 1,
#  'sigh': 1,
#  'Somewhere': 1,
#  'ages': 2,
#  'hence:': 1,
#  'Iâ€”': 1,
#  'less': 1,
#  'traveled': 1,
#  'by,': 1,
#  'has': 1,
#  'made': 1,
#  'all': 1,
#  'difference.': 1}
# """
# # **********************************************************************
# """
# Implement hash table where collisions are handled using linear probing. We learnt about linear probing
# in the video tutorial. Take the hash table implementation that uses chaining and modify methods to use
# linear probing. Keep MAX size of arr in hashtable as 10.
# """
# class HashTable:
#     def __init__(self):
#         self.MAX = 10  # I am keeping size very low to demonstrate linear probing easily but usually
#         # the size should be high
#         self.arr = [None for i in range(self.MAX)]
#
#     def get_hash(self, key):
#         hash = 0
#         for char in key:
#             hash += ord(char)
#         return hash % self.MAX
#
#     def __getitem__(self, key):
#         h = self.get_hash(key)
#         if self.arr[h] is None:
#             return
#         prob_range = self.get_prob_range(h)
#         for prob_index in prob_range:
#             element = self.arr[prob_index]
#             if element is None:
#                 return
#             if element[0] == key:
#                 return element[1]
#
#     def __setitem__(self, key, val):
#         h = self.get_hash(key)
#         if self.arr[h] is None:
#             self.arr[h] = (key, val)
#         else:
#             new_h = self.find_slot(key, h)
#             self.arr[new_h] = (key, val)
#         print(self.arr)
#
#     def get_prob_range(self, index):
#         return [*range(index, len(self.arr))] + [*range(0, index)]
#
#     def find_slot(self, key, index):
#         prob_range = self.get_prob_range(index)
#         for prob_index in prob_range:
#             if self.arr[prob_index] is None:
#                 return prob_index
#             if self.arr[prob_index][0] == key:
#                 return prob_index
#         raise Exception("Hashmap full")
#
#     def __delitem__(self, key):
#         h = self.get_hash(key)
#         prob_range = self.get_prob_range(h)
#         for prob_index in prob_range:
#             if self.arr[prob_index] is None:
#                 return  # item not found so return. You can also throw exception
#             if self.arr[prob_index][0] == key:
#                 self.arr[prob_index] = None
#         print(self.arr)
# """
# Function to show how *range(x, y) works.It returns a list of numbers in range(x, y)
# """
# [*range(5, 8)] + [*range(0, 4)]
# [5, 6, 7, 0, 1, 2, 3]
# t = HashTable()
# t["march 6"] = 20
# t["march 17"] = 88
# [None, None, None, None, None, None, None, None, None, ('march 6', 20)]
# [('march 17', 88), None, None, None, None, None, None, None, None, ('march 6', 20)]
# t["march 17"] = 29
# [('march 17', 29), None, None, None, None, None, None, None, None, ('march 6', 20)]
# t["nov 1"] = 1
# [('march 17', 29), ('nov 1', 1), None, None, None, None, None, None, None, ('march 6', 20)]
# t["march 33"] = 234
# [('march 17', 29), ('nov 1', 1), None, None, None, None, None, ('march 33', 234), None, ('march 6', 20)]
# t["dec 1"]
# t["march 33"]
# 234
# t["march 33"] = 999
# [('march 17', 29), ('nov 1', 1), None, None, None, None, None, ('march 33', 999), None, ('march 6', 20)]
# t["march 33"]
# 999
# t["april 1"] = 87
# [('march 17', 29), ('nov 1', 1), None, None, None, None, None, ('march 33', 999), ('april 1', 87), ('march 6', 20)]
# t["april 2"] = 123
# [('march 17', 29), ('nov 1', 1), ('april 2', 123), None, None, None, None, ('march 33', 999), ('april 1', 87),
#  ('march 6', 20)]
# t["april 3"] = 234234
# [('march 17', 29), ('nov 1', 1), ('april 2', 123), ('april 3', 234234), None, None, None, ('march 33', 999),
#  ('april 1', 87), ('march 6', 20)]
# t["april 4"] = 91
# [('march 17', 29), ('nov 1', 1), ('april 2', 123), ('april 3', 234234), ('april 4', 91), None, None, ('march 33', 999),
#  ('april 1', 87), ('march 6', 20)]
# t["May 22"] = 4
# [('march 17', 29), ('nov 1', 1), ('april 2', 123), ('april 3', 234234), ('april 4', 91), ('May 22', 4), None,
#  ('march 33', 999), ('april 1', 87), ('march 6', 20)]
# t["May 7"] = 47
# [('march 17', 29), ('nov 1', 1), ('april 2', 123), ('april 3', 234234), ('april 4', 91), ('May 22', 4), ('May 7', 47),
#  ('march 33', 999), ('april 1', 87), ('march 6', 20)]
# t["Jan 1"] = 0
#
# """
# ---------------------------------------------------------------------------
# Exception
# Traceback(most
# recent
# call
# last)
# < ipython - input - 131 - 8
# bb11a70eaa7 > in < module >
# ----> 1
# t["Jan 1"] = 0
#
# < ipython - input - 115 - 83
# ef0e71236e > in __setitem__(self, key, val)
# 27
# self.arr[h] = (key, val)
# 28 else:
# ---> 29
# new_h = self.find_slot(key, h)
# 30
# self.arr[new_h] = (key, val)
# 31
# print(self.arr)
#
# < ipython - input - 115 - 83
# ef0e71236e > in find_slot(self, key, index)
# 41
# if self.arr[prob_index][0] == key:
#     42
#     return prob_index
# ---> 43
# raise Exception("Hashmap full")
# 44
# 45
#
#
# def __delitem__(self, key):
#
#
# Exception: Hashmap
# full
# """
#
# del t["april 2"]
# [('march 17', 29), ('nov 1', 1), None, ('april 3', 234234), ('april 4', 91), ('May 22', 4), ('May 7', 47),
#  ('march 33', 999), ('april 1', 87), ('march 6', 20)]
# t["Jan 1"] = 0
# [('march 17', 29), ('nov 1', 1), ('Jan 1', 0), ('april 3', 234234), ('april 4', 91), ('May 22', 4), ('May 7', 47),
#  ('march 33', 999), ('april 1', 87), ('march 6', 20)]
# Implement hash table collision handling using linear probing
# class HashTable:
#     def __init__(self):
#         self.MAX = 10 # I am keeping size very low to demonstrate linear probing easily but usually the
#         # size should be high
#         self.arr = [None for i in range(self.MAX)]
#
#     def get_hash(self, key):
#         hash = 0
#         for char in key:
#             hash += ord(char)
#         return hash % self.MAX
#
#     def __getitem__(self, key):
#         h = self.get_hash(key)
#         if self.arr[h] is None:
#             return
#         prob_range = self.get_prob_range(h)
#         for prob_index in prob_range:
#             element = self.arr[prob_index]
#             if element is None:
#                 return
#             if element[0] == key:
#                 return element[1]
#
#     def __setitem__(self, key, val):
#         h = self.get_hash(key)
#         if self.arr[h] is None:
#             self.arr[h] = (key,val)
#         else:
#             new_h = self.find_slot(key, h)
#             self.arr[new_h] = (key,val)
#         print(self.arr)
#
#     def get_prob_range(self, index):
#         return [*range(index, len(self.arr))] + [*range(0,index)]
#
#     def find_slot(self, key, index):
#         prob_range = self.get_prob_range(index)
#         for prob_index in prob_range:
#             if self.arr[prob_index] is None:
#                 return prob_index
#             if self.arr[prob_index][0] == key:
#                 return prob_index
#         raise Exception("Hashmap full")
#
#     def __delitem__(self, key):
#         h = self.get_hash(key)
#         prob_range = self.get_prob_range(h)
#         for prob_index in prob_range:
#             if self.arr[prob_index] is None:
#                 return # item not found so return. You can also throw exception
#             if self.arr[prob_index][0] == key:
#                 self.arr[prob_index]=None
#         print(self.arr)
# Function to show how *range(x,y) works. It returns a list of numbers in range(x,y)
#
# [*range(5,8)] + [*range(0,4)]
# [5, 6, 7, 0, 1, 2, 3]
# t = HashTable()
# t["march 6"] = 20
# t["march 17"] =  88
# [None, None, None, None, None, None, None, None, None, ('march 6', 20)]
# [('march 17', 88), None, None, None, None, None, None, None, None, ('march 6', 20)]
# t["march 17"] = 29
# [('march 17', 29), None, None, None, None, None, None, None, None, ('march 6', 20)]
# t["nov 1"] = 1
# [('march 17', 29), ('nov 1', 1), None, None, None, None, None, None, None, ('march 6', 20)]
# t["march 33"] = 234
# [('march 17', 29), ('nov 1', 1), None, None, None, None, None, ('march 33', 234), None, ('march 6', 20)]
# t["dec 1"]
# t["march 33"]
# 234
# t["march 33"] = 999
# [('march 17', 29), ('nov 1', 1), None, None, None, None, None, ('march 33', 999), None, ('march 6', 20)]
# t["march 33"]
# 999
# t["april 1"]=87
# [('march 17', 29), ('nov 1', 1), None, None, None, None, None, ('march 33', 999), ('april 1', 87), ('march 6', 20)]
# t["april 2"]=123
# [('march 17', 29), ('nov 1', 1), ('april 2', 123), None, None, None, None, ('march 33', 999), ('april 1', 87), ('march 6', 20)]
# t["april 3"]=234234
# [('march 17', 29), ('nov 1', 1), ('april 2', 123), ('april 3', 234234), None, None, None, ('march 33', 999), ('april 1', 87), ('march 6', 20)]
# t["april 4"]=91
# [('march 17', 29), ('nov 1', 1), ('april 2', 123), ('april 3', 234234), ('april 4', 91), None, None, ('march 33', 999), ('april 1', 87), ('march 6', 20)]
# t["May 22"]=4
# [('march 17', 29), ('nov 1', 1), ('april 2', 123), ('april 3', 234234), ('april 4', 91), ('May 22', 4), None, ('march 33', 999), ('april 1', 87), ('march 6', 20)]
# t["May 7"]=47
# [('march 17', 29), ('nov 1', 1), ('april 2', 123), ('april 3', 234234), ('april 4', 91), ('May 22', 4), ('May 7', 47), ('march 33', 999), ('april 1', 87), ('march 6', 20)]
# t["Jan 1"]=0
# """
# ---------------------------------------------------------------------------
# Exception                                 Traceback (most recent call last)
# <ipython-input-131-8bb11a70eaa7> in <module>
# ----> 1 t["Jan 1"]=0
#
# <ipython-input-115-83ef0e71236e> in __setitem__(self, key, val)
#      27             self.arr[h] = (key,val)
#      28         else:
# ---> 29             new_h = self.find_slot(key, h)
#      30             self.arr[new_h] = (key,val)
#      31         print(self.arr)
#
# <ipython-input-115-83ef0e71236e> in find_slot(self, key, index)
#      41             if self.arr[prob_index][0] == key:
#      42                 return prob_index
# ---> 43         raise Exception("Hashmap full")
#      44
#      45     def __delitem__(self, key):
#
# Exception: Hashmap full
# """
# del t["april 2"]
# [('march 17', 29), ('nov 1', 1), None, ('april 3', 234234), ('april 4', 91), ('May 22', 4), ('May 7', 47), ('march 33', 999), ('april 1', 87), ('march 6', 20)]
# t["Jan 1"]=0
# [('march 17', 29), ('nov 1', 1), ('Jan 1', 0), ('april 3', 234234), ('april 4', 91), ('May 22', 4), ('May 7', 47), ('march 33', 999), ('april 1', 87), ('march 6', 20)]
# **************************************************************

"""
Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
"""
# from collections import deque
#
# class Stack:
#     def __init__(self):
#         self.container = deque()
#
#     def push(self, val):
#         self.container.append(val)
#
#     def pop(self):
#         return self.container.pop()
#
#     def peek(self):
#         return self.container[-1]
#
#     def is_empty(self):
#         return len(self.container) == 0
#
#     def size(self):
#         return len(self.container)
#
# def reverse_string(s):
#     stack = Stack()
#
#     for ch in s:
#         stack.push(ch)
#
#     rstr = ''
#     while stack.size()!=0:
#         rstr += stack.pop()
#
#     return rstr
#
#
# if __name__ == '__main__':
#     print(reverse_string("We will conquer COVID-19"))
#     print(reverse_string("I am the Python king"))
# *********************************************************************
"""
Write a function in python that checks if paranthesis in the string are balanced or not. 
Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
is_balanced("({a+b})")     --> True
is_balanced("))((a+b}{")   --> False
is_balanced("((a+b))")     --> True
is_balanced("))")          --> False
is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
"""
# from collections import deque
#
# class Stack:
#     def __init__(self):
#         self.container = deque()
#
#     def push(self, val):
#         self.container.append(val)
#
#     def pop(self):
#         return self.container.pop()
#
#     def peek(self):
#         return self.container[-1]
#
#     def is_empty(self):
#         return len(self.container) == 0
#
#     def size(self):
#         return len(self.container)
#
# def is_match(ch1, ch2):
#     match_dict = {
#         ')': '(',
#         ']': '[',
#         '}': '{'
#     }
#     return match_dict[ch1] == ch2
#
#
# def is_balanced(s):
#     stack = Stack()
#     for ch in s:
#         if ch=='(' or ch=='{' or ch == '[':
#             stack.push(ch)
#         if ch==')' or ch=='}' or ch == ']':
#             if stack.size()==0:
#                 return False
#             if not is_match(ch,stack.pop()):
#                 return False
#
#     return stack.size()==0
#
#
# if __name__ == '__main__':
#     print(is_balanced("({a+b})"))
#     print(is_balanced("))((a+b}{"))
#     print(is_balanced("((a+b))"))
#     print(is_balanced("((a+g))"))
#     print(is_balanced("))"))
#     print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
# ****************************************************************************

"""
Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. 
This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and 
print it. This thread serves an order every 2 seconds. 
Also start this thread 1 second after place order thread is started.
Use this video to get yourself familiar with multithreading in python

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']
This problem is a producer,consumer problem where place_order thread is producing orders 
whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.
"""
# import threading
# import time
#
# from collections import deque
#
# class Queue:
#     def __init__(self):
#         self.buffer = deque()
#
#     def enqueue(self, val):
#         self.buffer.appendleft(val)
#
#     def dequeue(self):
#         if len(self.buffer)==0:
#             print("Queue is empty")
#             return
#
#         return self.buffer.pop()
#
#     def is_empty(self):
#         return len(self.buffer) == 0
#
#     def size(self):
#         return len(self.buffer)
#
# food_order_queue = Queue()
#
# def place_orders(orders):
#     for order in orders:
#         print("Placing order for:",order)
#         food_order_queue.enqueue(order)
#         time.sleep(0.5)
#
#
# def serve_orders():
#     time.sleep(1)
#     while True:
#         order = food_order_queue.dequeue()
#         print("Now serving: ",order)
#         time.sleep(2)
#
# if __name__ == '__main__':
#     orders = ['pizza','samosa','pasta','biryani','burger']
#     t1 = threading.Thread(target=place_orders, args=(orders,))
#     t2 = threading.Thread(target=serve_orders)
#
#     t1.start()
#     t2.start()
# ******************************************************************************

"""
Write a program to print binary numbers from 1 to 10 using Queue. Use Queue class implemented in 
main tutorial. Binary sequence should look like,
    1
    10
    11
    100
    101
    110
    111
    1000
    1001
    1010
Hint: Notice a pattern above. After 1 second and third number is 1+0 and 1+1. 4th and 5th number are 
second number (i.e. 10) + 0 and second number (i.e. 10) + 1.

You also need to add front() function in queue class that can return the front element in the queue.
"""
# from collections import deque
#
# class Queue:
#     def __init__(self):
#         self.buffer = deque()
#
#     def enqueue(self, val):
#         self.buffer.appendleft(val)
#
#     def dequeue(self):
#         if len(self.buffer)==0:
#             print("Queue is empty")
#             return
#
#         return self.buffer.pop()
#
#     def is_empty(self):
#         return len(self.buffer) == 0
#
#     def size(self):
#         return len(self.buffer)
#
#     def front(self):
#         return self.buffer[-1]
#
# def produce_binary_numbers(n):
#     numbers_queue = Queue()
#     numbers_queue.enqueue("1")
#
#     for i in range(n):
#         front = numbers_queue.front()
#         print("   ", front)
#         numbers_queue.enqueue(front + "0")
#         numbers_queue.enqueue(front + "1")
#
#         numbers_queue.dequeue()
#
#
# if __name__ == '__main__':
#     produce_binary_numbers(10)
# ************************************************************************
"""
Data structures exercise: General Tree
Below is the management hierarchy of a company.
"""
# class TreeNode:
#     def __init__(self, name, designation):
#         self.name = name
#         self.designation = designation
#         self.children = []
#         self.parent = None
#
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent
#
#         return level
#
#     def print_tree(self, property_name):
#         if property_name == 'both':
#             value = self.name + " (" + self.designation + ")"
#         elif property_name == 'name':
#             value = self.name
#         else:
#             value = self.designation
#
#         spaces = ' ' * self.get_level() * 3
#         prefix = spaces + "|__" if self.parent else ""
#         print(prefix + value)
#         if self.children:
#             for child in self.children:
#                 child.print_tree(property_name)
#
#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)
#
# def build_management_tree():
#     # CTO Hierarchy
#     infra_head = TreeNode("Vishwa","Infrastructure Head")
#     infra_head.add_child(TreeNode("Dhaval","Cloud Manager"))
#     infra_head.add_child(TreeNode("Abhijit", "App Manager"))
#
#     cto = TreeNode("Chinmay", "CTO")
#     cto.add_child(infra_head)
#     cto.add_child(TreeNode("Aamir", "Application Head"))
#
#     # HR hierarchy
#     hr_head = TreeNode("Gels","HR Head")
#
#     hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
#     hr_head.add_child(TreeNode("Waqas", "Policy Manager"))
#
#     ceo = TreeNode("Nilupul", "CEO")
#     ceo.add_child(cto)
#     ceo.add_child(hr_head)
#
#     return ceo
#
#
# if __name__ == '__main__':
#     root_node = build_management_tree()
#     root_node.print_tree("name")
#     root_node.print_tree("designation")
#     root_node.print_tree("both")
# ***************************************************
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         self.parent = None
#
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent
#
#         return level
#
#     def print_tree(self, level):
#         if self.get_level() > level:
#             return
#         spaces = ' ' * self.get_level() * 3
#         prefix = spaces + "|__" if self.parent else ""
#         print(prefix + self.data)
#         if self.children:
#             for child in self.children:
#                 child.print_tree(level)
#
#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)
#
# def build_location_tree():
#     root = TreeNode("Global")
#
#     india = TreeNode("India")
#
#     gujarat = TreeNode("Gujarat")
#     gujarat.add_child(TreeNode("Ahmedabad"))
#     gujarat.add_child(TreeNode("Baroda"))
#
#     karnataka = TreeNode("Karnataka")
#     karnataka.add_child(TreeNode("Bangluru"))
#     karnataka.add_child(TreeNode("Mysore"))
#
#     india.add_child(gujarat)
#     india.add_child(karnataka)
#
#     usa = TreeNode("USA")
#
#     nj = TreeNode("New Jersey")
#     nj.add_child(TreeNode("Princeton"))
#     nj.add_child(TreeNode("Trenton"))
#
#     california = TreeNode("California")
#     california.add_child(TreeNode("San Francisco"))
#     california.add_child(TreeNode("Mountain View"))
#     california.add_child(TreeNode("Palo Alto"))
#
#     usa.add_child(nj)
#     usa.add_child(california)
#
#     root.add_child(india)
#     root.add_child(usa)
#
#     return root
#
#
# if __name__ == '__main__':
#     root_node = build_location_tree()
#     root_node.print_tree(3)