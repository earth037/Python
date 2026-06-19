# a = [1,2,3,4,]
# print(a)
# print(type(a))
# #ordered - everything that is stored are in a order.
# #mutable
# l = [10,20,31,40,50]
# print(l)
# l[2] = 30
# print(l)

# #duplicate
# l = [1,1,1,1,2,2,2,2,3,3,3,3,34,4,4,45,5,5,5]
# print(l)

#traversing on list
#traversing on values
# a = [10,20,30,40,50]
# for i in a:
#     print(i)

# #traversing on values
# for i in range(len(a)):
#     print(f"{i}:{a[i]}")

# l = [1,3,2,4,5,6,9,7]
# l.append(0)
# l.append("hello")
# print(l)
# l.insert(2,15)
# print(l)
# l.remove(15)
# print(l)
# a = l.pop(4)
# print(l)
# print(a)
# l.clear()
# print(l)
# l = [1,3,2,4,5,6,9,7]
# l.sort()
# print(l)
# l.reverse()
# print(l)
# print(len(l))

#Print all positive and negative elements separately.
# l = [1,3,2,5,-3,5,-4,-6,-7]
# positive = []
# negative = []
# for i in range(len(l)):
#     if l[i] >= 0:
#         positive.append(l[i])
#     else:
#         negative.append(l[i])
# print(positive)
# print(negative)

#Find the mean (average) of all list elements.
# l = [1,3,2,5,-3,6,10,8]
# sum = 0
# for i in range(len(l)):
#     sum += l[i]
# avg = sum / len(l)
# print(avg)

#Find the greatest element and print its index.
# l = [1,3,2,5,-3,6,10,8]
# g = l[0]
# index = 0
# for i in range(len(l)):
#     if l[i] > g:
#         g = l[i]
#         index = i
# print(f"largest element is {g} at index {index}")

#Find the second greatest element.
# l = [1,9,2,5,-3,6,10,8]
# le = l[0]
# sle = l[0]
# ile = 0
# isle = 0
# for i in range(len(l)):
#     if l[i] > le:
#         sle = le
#         isle = ile
#         le = l[i]
#         ile = i
#     elif l[i] > sle:
#         sle = l[i]
#         isle = ile
# print(f"largest no. is {le} at index {ile} and second largest no. is {sle} at index {isle}")

#Check if the list is already sorted.
# a = [10,20,30,25,50]
# for i in range(len(a)-1):
#     if a[i] > a[i+1]:
#         print("your list is not sorted")
#         break
# else:
#     print("your list is sorted")
