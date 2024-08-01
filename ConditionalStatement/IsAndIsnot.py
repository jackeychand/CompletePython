a = 10
b = 10
c = 20
print(id(a))
print(id(b))
print(id(c))

if a is b:
    print("true")
else:
    print("false")
i = input("enter number")        
j = input("enter number")
print(id(i))
print(id(j))
if i is j:
    print("True")