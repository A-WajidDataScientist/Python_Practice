# Print  \
# *
# **
# ***
# ****

rows = int(input("Enter rows num = "))

for i in range(1, rows + 1):
    for j in range(0, i):
        print("*", end=" ")

    print("")
