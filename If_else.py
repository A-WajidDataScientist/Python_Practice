# Exercise: Python If Condition

# Q1. Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# i. Write a program that asks user to enter a city name and it should tell which country the city belongs to
# ii. Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
#     For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and
#     dhaka it should print "They don't belong to same country"


# i
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore", "karachi", "islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]

# city = input("Enter the city name:")
# if city == "lahore" or city == "karachi" or city == "islamabad":
#     print("country name : Pakistan")
# elif city == "lahore" or city == "karachi" or city == "islamabad":
#     print("country name : Bangladesh")
# elif city == "mumbai" or city == "banglore" or city == "chennai" or city == "delhi":
#       print("country name : India")
# else:
#     print("Not in record")

# ii
# city_1 = input("Enter the city name:")
# city_2 = input("Enter the city name:")
# if city_1 in india and city_2 in india:
#     print("country name : India")
# elif city_1 in pakistan and city_2 in pakistan:
#     print("country name : Pakistan")
# elif city_1 in bangladesh and city_2 in bangladesh:
#     print("country name : Bangladesh")
# else:
#     print("Not in record")

# Q2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
# i. Ask user to enter his fasting sugar level
# ii. If it is below 80 to 100 range then print that sugar is low
# iii. If it is above 100 then print that it is high otherwise print that it is normal

sugar_level = int(input("Enter your sugar level:"))
if sugar_level < 80:
    print("your sugar is low")
elif sugar_level in range(80, 100):
    print("your sugar is Normal")

elif sugar_level > 100:
    print("your sugar is high")
