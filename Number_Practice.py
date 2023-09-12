# Exercise: Numbers in python
# Q1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
# Q2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar.
# Find out using python, how many dollars is the shopkeeper going to give you back?
# Q3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length.
# If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles.
# Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)

# solution
#  Q1:
length = 92
width = 48.8
area = length*width
print("Area: ", round(area, 2))

# Q2:
bought = 9
costs = 1.49
give = 20

my_return = give - bought*costs

print("your return ", my_return)

# Q3
area = 5.5 ** 2
cost = 500  # rs per square feet
total_cost = area * cost
print(total_cost)
