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
