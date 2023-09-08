# # Python Program to Find the Square

# a = 1
# while (a == 1 or a != 1) and a != 0:
#     a = int(input("Enter 1 for continue Or 0 for exist "))

#     if (a == 1 or a != 1) and a != 0:

#         num = int(input("Enter number num = "))
#         sq = num * num
#         print("square = ", sq)

#     else:
#         print("calculation ended")

# Python Program to Find the Square Root
import math
a = 1
while (a == 1 or a != 1) and a != 0:
    a = int(input("Enter 1 for continue Or 0 for exist "))

    if (a == 1 or a != 1) and a != 0:

        num = int(input("Enter number num = "))
        print("square root = ", math.sqrt(num))

    else:
        print("calculation ended")
