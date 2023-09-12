# Exercise: Python User Input
# Q1. Write a program that can find area of a triangle. It should take base and height as an input from user
# and using that it should print an area of a triangle
# Q2. Write a program that takes file name with extension as an input and prints just the file name without
# extension (you can assume that file extensions are always 3 character long)

# Solution:
# Q1

# print("Calcultion of Tringle Area")
# base = float(input("Enter the base:"))
# height = float(input("Enter the height:"))
# cal = 1/2*base*height
# print("Tringle Area: ", cal)

#Q2
file_name = input("Enter file name witn extension: ")
print(file_name[:file_name.find(".")])