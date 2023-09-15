# # Exercise: Functions in python

# # Q1:Write a function called calculate_area that takes base and height as an input and returns and area of a triangle.
# #    Equation of an area of a triangle is, area = (1/2)*base*height

# def calculate_area(base, height):
#     area = (1/2)*base*height
#     print("Area of tringle: ", area)


# t_base = float(input("Enter base of tringle: "))
# t_height = float(input("Enter height of tringle: "))
# calculate_area(t_base, t_height)


# # Q2: Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on
# #     shape type it will calculate area. Equation of rectangle's area is, rectangle area=length*width
# #     If no shape is supplied then it should take triangle as a default shape


# def calculate_area(base, height):
#     shape = input("Enter shape: ")
#     if shape == "rectangle":
#         area = base*height
#         print("Area of Rectangle: ", area)
#     else:
#         area = (1/2)*base*height
#         print("Area of tringle: ", area)


# t_base = float(input("Enter base of tringle: "))
# t_height = float(input("Enter height of tringle: "))
# calculate_area(t_base, t_height)


# # Q3: Write a function called print_pattern that takes integer number as an argument and prints following pattern
# #     if input number is 3,
# # *
# # **
# # ***
# # if input is 4 then it should print
# # *
# # **
# # ***
# # ****
# # Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)
def print_pattern(input_num):

    for i in range(1, input_num+1):
        s = ""
        for j in range(i):
            s += "*"
        print(s)


input_num = int(input("Enter num to print the pattern line: "))
print_pattern(input_num)
