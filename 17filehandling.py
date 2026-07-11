# open("hello.txt","x")
# file = open("hello2.txt","w")
# data = input("what do you want to write: ")
# file.write(data)
# file = open("hello2.txt","r")
# print(file.read())
with open("hello2.txt","a") as f:
    f.write(", " + "is best bgmi player")