i = 1
print(i)
print(type(i))
print(i.__sizeof__())


# float
a = 5.6
print(type(a))
print(a.__sizeof__())

b= -2.4
print(b)
c= 34345435353.2
print(c.__sizeof__())

d= 2.3 * 100
print(d)

e = 0.1259E2    #scentific represention
print(e)

#Boolean
a = True
print(a)
print(type(a))
print(a.__sizeof__())
print(int(a))

# Complex Number

a= 3 + 5j
print(a)
print(type(a))
print(a.__sizeof__())


# use of underscore in integer
d = 342_343
print(d)
print(type(d))

e = '1234242'
print(e)
print(int(e))
print(type(e))

f = 5.6
print(type(int(f)))
print(type(f))


# used for converting to Binary number
c = 34
print(bin(c))