# for i in range(11):
#     print(i)
# for i in range(5,11):
#     print(i)
# for i in range(0,11,2):
#     print(i)

# for i in range(5,51,5):
#     print(i)

# a = int(input("enter a number: "))
# for i in range(a, (a*10)+1,a):
#     print(i)

#For loop on string
# a = "Hello"
# for i in a:
#     print(i)
# for i in range(len(a)):
#     print(i)
# for i in range(len(a)):
#     print(a[i])

# for i in range(1,11):
#     if i == 4:
#         break
#     print(i)

# for i in range(1,11):
#     if i == 4:
#         continue
#     print(i)

# for i in range(1,11):
#     if i == 45:
#         break
#     print(i)
# else:
#     print("no break was encountered")

#Print "Hello World" n times.
# n = int(input("enter a number: "))
# for i in range(n):
#     print("Hello World")

#Print natural numbers from 1 to n.
# n = int(input("enter a number: "))
# for i in range(1,n+1):
#     print(i)

#Reverse for loop — print n down to 1.
# n = int(input("enter a number: "))
# for i in range(n,0,-1):
#     print(i)

#Print the multiplication table of a number.
# n = int(input("enter a number: "))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}")

#Sum of first n natural numbers.
# n = int(input("enter a number: "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)

#Factorial of a number.
# n = int(input("enter a number: "))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print(fact)

#Print sum of all even and odd numbers in a range separately.
# n = int(input("enter a number: "))
# evensum = 0
# oddsum = 0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         evensum += i
#     else:
#         oddsum += i
# print(f"EvenSum is {evensum} and OddSum is {oddsum}")

#Print all factors of a number.
# n = int(input("enter a number: "))
# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)

#Check if a number is perfect (sum of factors = the number itself).
# n = int(input("enter a number: "))
# sum = 0
# for i in range(1,n):
#     if n % i == 0:
#         sum += i
# if sum == n:
#     print("perfect number")
# else:
#     print("not a perfect number")

#Check if a number is prime.
# n = int(input("enter a number: "))
# count = 0
# for i in range(1,n+1):
#     if n % i == 0:
#         count += 1
# if count == 2:
#     print("prime number")
# else:
#     print("not a prime number")

#Reverse a string without using built-in functions.
# s = input("enter a string: ")
# r = ""
# for i in range(len(s)-1,-1,-1):
#     r += s[i]
# print(r)

#Check if a string is a palindrome.
# s = input("enter a string: ")
# r = ""
# for i in range(len(s)-1,-1,-1):
#     r += s[i]
# if s == r:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

#Count letters, digits, and special symbols in a string.
# a = input("enter a string: ")
# char = 0
# spchar = 0 
# digits = 0
# for i in a:
#     if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
#         char += 1 
#     elif ord(i) >= 48 and ord(i) <= 90:
#         digits += 1
#     else:
#         spchar = spchar + 1

# print(f"characters {char} , special characters - {spchar}, digits - {digits}")