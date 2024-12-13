# E1
# def area(length,width):
#    result = length * width
#    print(result)

# w = int(input("Please add width: "))
# l = int(input("Please add length: "))
# area(l,w)

# E2
# def details(c):
#    f = (9/5 * c) + 32
#    print(f) 

# c = int(input("Please add celcium: "))
# details(c)

# E3
# def numbers(a, b, c):
#     formula = (a + b + c) / 3
#     return formula

# a = int(input("Please add first number: "))
# b = int(input("Please add second number: "))
# c = int(input("Please add third number: "))

# result = numbers(a, b, c)
# print(f"The average is: {result}")

# E4
# def find_primes(x):
#     for i in range (x):
#         if i%2 != 0:
#             print(i)

# num = int(input("Please enter a number, and I will find all prime numbers up to it! "))

# find_primes(num)

# M1
# def calculator(a, b, operation):
#     if operation == "add":
#         return a + b
#     elif operation == "subtract":
#         return a - b
#     elif operation == "multiply":
#         return a * b
#     elif operation == "divide":
#         if b != 0:
#             return a / b
#         else:
#             return "Error: Division by zero is not allowed."
#     else:
#         return "Error: Invalid operation."

# a = int(input("Please add the first number: "))
# b = int(input("Please add the second number: "))

# operation = input("Choose an operation (add, subtract, multiply, divide): ").lower()

# result = calculator(a, b, operation)


# print(f"The result is: {result}")

# M2

# def prime (number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

# number = int(input("Enter a number to check if it's prime: "))

# result = prime(number)
# print(f"If {number} is prime you will see True, if not False: {result}")

#  M3
# def palindrome(text):
#   return text == text[::-1]

# text = input("Enter a word: ").replace(" ", "").lower()
# print(f"Is it a palindrome? {palindrome(text)}")







