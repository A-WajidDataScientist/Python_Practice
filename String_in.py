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
print(dir(str))

# Exercise: String in Python
# Q1. Create 3 variables to store street, city and country, now create address variable to store entire address.
# Use two ways of creating this variable, one using + operator and the other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line
# Q2. Create a variable to store the string "Earth revolves around the sun"
# Q3. Print "revolves" using slice operator
# Q4. Print "sun" using negative index
# Q5. Create two variables to store how many fruits and vegetables you eat in a day.
# Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.

# sollution:
# Q1
street = "Street: Raza-Bazaar "
city = "City: chak "
country = "Pakistan"
address = street+city+country
print(address)
print(f"Address: {street}{city}{country}")


# Q2
txt = "Earth revolves around the sun"
print(txt)

# Q3
print(txt[6:15])

# Q4
print(txt[-3:])

# Q5
y = "2"
x = "3"

print(f"I eat {x} veggies and {y} fruits daily")


# Q6. I have a string variable called s='maine 200 banana khaye'.
# This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'.
# Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.

s = 'maine 200 banana khaye'
s = s.replace(" 200", " 10")
s = s.replace(" banana", " samosa")
print(s)


s = s.replace(" 200 banana", " 10 samosa")

print(s)
