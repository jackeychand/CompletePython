n = int(input("enter number"))
count = 0
for i in range(1, n+1):
    if n%i == 0:
        count+=1
        print(count)
if count ==2:
    print("Prime") 
else:
    print("Not Prime")       