# a = int(input("your age?"))
# if a>=18:
#     print("you can vote")
# else:
#     print("you cannot vote")

#Accept two numbers and print the greatest between them.
# a = int(input("first no. :"))
# b = int(input("second no. :"))
# if a == b:
#     print("they are equal")
# elif a > b:
#     print(f"{a} is greater")
# else:
#     print(f"{b} is greater")

#Accept gender from user and print a greeting message.
# a = input("your gender M or F:")
# if a == "M" or a == "m":
#     print("Good Morning Sir")
# elif a == "F" or a == "f":
#     print("Good Morning Ma'am")
# else:
#     print("Wrong Value Entered")

#Accept an integer and check if it is even or odd.
# a = int(input("enter a number: "))
# if a%2==0:
#     print("Even number")
# else:
#     print("Odd number")

#Accept name and age — check if the user is a valid voter (18+).
# name = input("Name: ")
# age = int(input("Age: "))
# if age >= 18:
#     print(f"Hello {name}, you are a valid voter")
# else:
#     print(f"Hello {name}, you can vote after {18-age} years")

#Accept a year and check if it is a leap year.
# y = int(input("Enter a year: "))
# if y % 100 == 0 and y % 400 == 0:
#     print("Leap Year")
# elif y % 4 == 0 and y % 100 != 0:
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

#Accept temperature in °C and print a description.
t = int(input("Enter temperature in degree celcius"))
if t <= 5 and t >= -5:
    print("very cold")
elif t >= 6 and t <= 18:
    print("cold")
elif t >= 19 and t <= 40:
    print("hot")
elif t >= 41 and t <= 50:
    print("very hot")