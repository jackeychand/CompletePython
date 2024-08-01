amount = int(input("enter the amount "))

if amount <=10000:
    print(f" discount of 10 percent is ", amount*10/100)
elif amount >=10000 and amount <=20000:
    print(f" discount of 20 percent is ", amount*20/100)
elif amount >=20000 and amount <=30000:
    print(f" discount of 30 percent is ", amount*30/100)
else:
    print(f" discount of 50 percent is ", amount*50/100)    