# # Exercise: Python for loop

# # Q1: After flipping a coin 10 times you got this result,
# # result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# # Using for loop figure out how many times you got heads

# result = ["heads", "tails", "tails", "heads", "tails",
#           "heads", "heads", "tails", "tails", "tails"]
# count = 0
# for i in result:
#     if i == "heads":
#         count += 1
# print("We got heads", count, "times")


# # Q2: Print square of all numbers between 1 to 10 except even numbers

# for i in range(1, 10, 2):
#     print("Odd num square:", i**2)

# # Q3: Your monthly expense list (from Jan to May) looks like this,expense_list = [2340, 2500, 2100, 3100, 2980]
# # Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred.
# # If expense is not found then it should print that as well.
# month_list = ["January", "February", "March", "April", "May"]
# expense_list = [2340, 2500, 2100, 3100, 2980]
# e = input("Enter expense amount: ")
# e = int(e)

# month = 0
# for i in range(len(expense_list)):
#     if e == expense_list[i]:
#         month = i
#         break

# if month != 0:
#     print(f'You spent {e} in {month_list[month]}')
# else:
#     print(f'You didn\'t spend {e} in any month')

# # Q4: Lets say you are running a 5 km race. Write a program that,
# # i. Upon completing each 1 km asks you "are you tired?"
# # ii. If you reply "yes" then it should break and print "you didn't finish the race"
# # iii. If you reply "no" then it should continue and ask "are you tired" on every km
# # iv. If you finish all 5 km then it should print congratulations message
# for i in range(5):
#     print(f"You ran {i+1} miles")  # i starts with zero hence adding 1
#     tired = input("Are you tired? ")
#     if tired == 'yes':
#         break

# if i == 4:  # 4 because the index starts from 0
#     print("Hurray! You are a rock star! You just finished 5 km race!")
# else:
#     print(
#         "You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles")

# # Q5:Write a program that prints following shape

# # *
# # **
# # ***
# # ****
# # *****

for i in range(1, 6):
    # Initialize an empty string 's' for each iteration of the outer loop
    s = ''
    for j in range(i):
        s += '*'
    print(s)
