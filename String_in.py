# Creating String
c = str("hello")
print(c)
c = str('hello')
print(c)
c = str("""hello""")  # this is use for multi_lines
print(c)
c = str('''hello''')
print(c)
c = str("he'llo")
print(c)
c = str('"hello"')
print(c)


# Accessing Substring from a String
# String index start form 0 to 1
# Types positve (Left to right) and negative (right to Left) indexing

print(c[1])
print(c[-2])

# Slicing
# multiple character extract from the string

c = "hello world"
print(c[0:4])
print(c[0:4:2])

# 0 for start, 4 end means 3 character only & 2 is skip only on character

# Editing & deleting character

# String are a Immutable Data Type

# deleting

c = "hello"
del c

# Operation on string
#  Arithmetic Operations
#  Relational Operations
#  Logical Operations
#  Loops on Strings
#  Membership Operations


# common functions
# len (total length)
# max
# min
# sorted
c = "Abdul Wajid"

print(len(c))
print(max(c))
print(min(c))
print(sorted(c))  # ascending order
print(sorted(c))  # descending order

# Capitalize/Title/Upper/Lower/Swapcase
print("it is raining".capitalize())
print("it is raining".title())
print("it is raining".upper())
print("IT IS RAINING".lower())
print("It Is RaininG".swapcase())

# count
print("it is raining".count("ing"))
print("it is raining".count("i"))
print("it is raining".count("x"))

# Find/Index
print("it is raining".find("i"))
print("it is raining".find("a"))
print("it is raining".find("x"))
print("it is raining".index("a"))

#
