# count = 1
# while count <= 5:
#     print(count)
#     count += 1

#Separate each digit of a number and print on a new line.
# n = int(input("enter a number: "))
# while n > 0:
#     print(n%10)
#     n = n//10

#Accept a number and print its reverse.
# n = int(input("enter a number: "))
# rev = 0
# while n > 0:
#     rev = rev * 10 + n % 10
#     n = n//10
# print(rev)

#Check if a number is palindromic (equal to its reverse).
n = int(input("enter a number: "))
c = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n//10
if c == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")