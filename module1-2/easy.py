# Excercise1 - Number is even or odd

# num = int(input("Please enter a number: "))
# if num % 2 == 0:
#     print("Number is even")
# else:
#     print("Number is odd")

# Excercise2 - Categorize a number

# num = int(input("please enter a number:  "))
# if num > 0:
#     print ("Your number is positive")
# elif num < 0:
#     print ("Your number is negative")
# else:
#     print ("Your number is Zero")

# Excercise3 - Determine the largest number

# x = int(input("Please add first number: "))
# y = int(input("Please add second number: "))
# z = int(input("Please add third number: "))

# if x > y and x > z:
#     print(f"The biggest number is {x}")
# elif y > x and y > z:
#     print(f"The biggest number is {y}")
# else:
#     print(f"The biggest number is {z}")

# Excercise4 - Determine if a Year is a Leap year

# year = int(input("Please enter a year: "))
# if year % 4 == 0:
#     print (f"{year} is a leap year")
# else:
#     print (f"{year} is not a leap year")

# Excercise5 - Print even numbers

# for num in range(2, 21): 
#     if num % 2 == 0:
#         print(f"{num} is an even number between 2 and 20")

# Excercise6 - Countdown from 10 to 1 

# for num in reversed(range(1,11)):
#     print(num)

# Middle1 - Determine the season

# month = int(input("Please add a month as a number from 1 to 12: "))

# if month in range(1, 3) or month == 12:
#     print(f"{month} is in the Winter season")
# elif month in range(3, 6):
#     print(f"{month} is in the Spring season")
# elif month in range(6, 9):
#     print(f"{month} is in the Summer season")
# elif month in range(9, 12):
#     print(f"{month} is in the Autumn season")
# else:
#     print("Invalid month. Please enter a number between 1 and 12.")

#Middle2 Check eligibility for driving

# age = int(input("Please enter your age: "))
# license = input("Do you have a driving license? (yes or no): ")

# if age >= 18 and license == "yes":
#     print("You are eligible to drive a car")
# else:
#     print("Unfortunately, you are not eligible to drive a car")

# Middle3 Categorize a triangle

# x = int(input("Please enter first the length of one side of the triangle: "))
# y = int(input("Please enter length of the second side the triangle: "))
# z = int(input("Please enter length of the third side the triangle: "))

# if x == y == z:
#     print("Your triangle is Equilateral")
# elif x == y or x == z or y == z:
#     print("Yout triangle is Isosceles")
# else:
#     print("Your triangle is Scalene")

# Middle4 Print a pattern

# def print_patterns(count):
#     for i in range(count):
#         number_as_string = str(i+1)
#         print(number_as_string * (i+1))


# print_patterns(6)
      
# Middle5 Check for polindromes

# txt = input("Please enter a word that you want to check: ")

# if txt == txt[::-1]:
#     print(f"{txt} is a palindrome")
# else:
#     print(f"{txt} is not a palindrome")

# Middle6 Discount for a movie ticket

# age = int(input("Please enter your age: "))
# student = input("Do you have a student ID? (yes or no): ")

# if age < 12:
#     print("Ticket price for you is 5$")
# elif 11 < age < 18 and student == "yes":
#     print("Ticket price for you is 7$")
# elif 11 < age < 18 and student == "no":
#     print("Ticket price for you is 9$")
# else:
#     print("Ticket price for you is 12$")

# Advance1 Zodiac Sign 

# month = int(input("please enter your birth month(mm): "))
# day = int(input("please enter your birth day(dd): "))

# if month < 1 or month > 12:
#     print("Invalid month. Please enter a month between 1 and 12.")
# elif day < 1 or day > 31:
#     print("Invalid day. Please enter a day between 1 and 31.")
# elif (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
#     print("Invalid day. This month has only 30 days.")
# elif month == 2 and day > 29:
#     print("Invalid day. February has only 28 or 29 days.")           
# if (month == 3 and day >= 21) or (month == 4 and day <= 19):
#     print("Aries")
# elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
#     print("Taurus")
# elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
#     print("Gemini")
# elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
#     print("Cancer")
# elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
#     print("Leo")
# elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
#     print("Virgo")
# elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
#     print("Libra")
# elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
#     print("Scorpio")
# elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
#     print("Sagittarius")
# elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
#     print("Capricorn")
# elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
#     print("Aquarius")
# elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
#     print("Pisces")
# else:
#     print("Invalid date")

# Advance3 Number pyramid

# def print_number_pyramid(rows):
#     for i in range(1, rows + 1):
       
#         for j in range(i, 2 * i):
#             print(j, end="")
        
#         for j in range(2 * i - 2, i - 1, -1):
#             print(j, end="")
        
#         print()

# rows = 11
# print_number_pyramid(rows)