no = int(input("enter the total number"))

count = 0
max = 0
max = int(input("enter maximum"))   #this is used for negative value
while count < no-1:
    num = int(input("enter the number "))
    if num>max:
        max =num
    count = count + 1
print("maximun", max)        