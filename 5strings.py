a = "h"
print(ord(a))

#indexing - 0,1,2,3,... left to right and -1,-2,-3,... right to left
s = "prithvi"
print(s[0]) #p
print(s[1]) #r
print(s[-1]) #i
print(s[-2],s[1]) #v r
print(s[0:3:1]) #pri
print(s[0:3:2]) #pi
print(s[-2:-6:-1]) #vhti
print(s[::2]) #pihi
r = "python is great"
print(r[0:6]) #python
print(r[7:9]) #is
print(r[10:15]) #great

#Type Conversion
a = "123"
print(type(a)) #str
b = int(a)
a = int(a)
print(type(b)) #int
print(type(a)) #int

c = 3.14
print(type(c)) #float
d = int(c)
print(type(d)) #int
print(d) #3

e = 22
print(type(e)) #int
f = 3.15
print(type(f)) #float
g = 3 + 4j
print(type(g)) #complex
h = True
print(type(h)) #bool
i = None
print(type(i)) #NoneType
e = str(e)
f = str(f)
g = str(g)
h = str(h)
i = str(i)
print(type(e)) #str
print(type(f)) #str
print(type(g)) #str
print(type(h)) #str
print(type(i)) #str

a = 12
b = 0
c = 3.14
d = 0.0
e = ""
f = "hello"
g = []
h = ()
i = {}
j = None
print(bool(a)) #True
print(bool(b)) #False
print(bool(c)) #True
print(bool(d)) #False
print(bool(e)) #False
print(bool(f)) #True
print(bool(g)) #False
print(bool(h)) #False
print(bool(i)) #False
print(bool(j)) #False

#implicit type conversion
a = 22
b = a/2
print(type(a)) #int
print(type(b)) #float
print(b) #11.0
