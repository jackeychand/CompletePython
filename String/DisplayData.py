name = input("enter the name ")
price = input('enter price')

totallength = len(name)+len(price)

dots = '*'*(25-totallength)
print(name+dots+price)