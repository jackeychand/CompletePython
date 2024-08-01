num = int(input("enter number"))
num1 = num

pan = 0

while num>0:
    r = num % 10
    num = num // 10
    pan = pan * 10 + r
print(pan) 

if num1 is pan:
    print("palindrome")
else:
    print("Not palindrome")    