# d = {1:11,2:20,3:30,4:40}
# Vanilla python
# print(d)
# d[5] = 50
# print(d)
# print(d[2])
# d[1] = 10
# print(d)

#methods approach
# print(d.get(2))
# print(d.items())
# print(d.keys())
# print(d.values())
# print(d.pop(3))
# print(d.popitem())
# print(d.setdefault(6,3000))
# print(d)
# d.update({3:35})
# print(d)
# q = d.fromkeys([1,2],15)
# print(q)

#traversing (loops)
# for i in d:
#     print(f"keys {i} and values {d[i]}")

#Merge two dictionaries into one.
# d1 = {"a":1,"b":2,"c":3}
# d2 = {"c":4,"d":2,"e":3}

# for i in d2:
#     d1[i] = d2[i]
# print(d1)

#Sum all values in a dictionary.
# d = {1:11,2:20,3:30,4:40}
# sum = 0
# for i in d:
#     sum += d[i]
# print(sum)

#Count the frequency of each element in a list using a dictionary.
# l = ["a","b","a","c","b","a","c","a","b"]
# d = {}
# for i in l:
#     if i in d.keys():
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1
# print(d)

#Combine two dicts, adding values for common keys.
# d1 = {"a":1,"b":2,"c":3}
# d2 = {"c":4,"d":2,"e":3}
# for i in d2:
#     if i in d1.keys():
#         d1[i] = d1[i] + d2[i]
#     else:
#         d1[i] = d2[i]
# print(d1)