numberOfNumber = int(input("enter the number"))
count = 0
psum = 0
nsum = 0

while numberOfNumber > count:
    n = int(input("enter the digit"))
    if n >= 0:
        psum = psum + n
        count =count + 1
    else:
        nsum = nsum + n
        count =count + 1    

print("sum of Postive digit", psum)
print("sum of neagtive digit", nsum)
print("count of digit", count) 