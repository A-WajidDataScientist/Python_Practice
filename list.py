# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

L = [1, 2, 3, 4]
print(L)
L[0] = 10
print(L)

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:

# Example
# Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(3, 100)
print(thislist)

thislist.extend(L)
print(thislist)


# Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list


# Exercise: Python Lists

# Q1
# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
#    got a refund of 200$. Make a correction to your monthly expense list
#    based on this

# 1:
monthly_expenses = ["January - ", 2200, "February - ",
                    2350, "March - ", 2600, "April - ", 2130, "May - ", 2190]
print("In feb extra dollars spents:",
      monthly_expenses[3]-monthly_expenses[1], "dollars")
# 2:
# method_1
print("Total expense in first quarter of the year:",
      monthly_expenses[1]+monthly_expenses[3]+monthly_expenses[5], "dollars")
# method_2
sum_q = monthly_expenses[1:7:2]
print("Total expense in first quarter of the year:",
      sum_q[0]+sum_q[1]+sum_q[2], "dollars")

# 3:
print(2000 in monthly_expenses)


# 4:
monthly_expenses.append("June")
monthly_expenses.append(1980)

# 5:
corr = monthly_expenses[7]-200
print(monthly_expenses)
monthly_expenses[7] = corr
print("After correction:", monthly_expenses)

# Q2. You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
print("List length: ", len(heros))
heros.append("black panther")
print(heros)
heros.remove("black panther")
print(heros)
heros.insert(3, "black panther")
print(heros)
heros.remove("hulk")
print(heros)
heros[1] = "doctor strange"
print(heros)
# heros.sort()
print(sorted(heros))
