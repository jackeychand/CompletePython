num = int(input("enter the number"))
count = 0
while num > 0:
    num = num // 10
    count +=1
print("length of number is ", count)    