# # this will work only with odd number bcz first occurance of 0 leads to 0*10
# num = int(input("enter the number for Binary conversion "))
# bin = 0
# while num>0:
#     r = num% 2
#     num =num //2
#     bin =bin *10+r
# print("binary value", bin)
# rev =0

# while bin>0:
#     r = bin%10
#     bin= bin//10
#     rev =rev*10+r
# print("binary reverse value", rev)

# this will work with every numbe

num = int(input("enter the number for Binary conversion "))
bin = ''
while num>0:
    r = num% 2
    num =num //2
    bin =str(r)+bin
print("binary value", bin)
# rev =0

# while bin>0:
#     r = bin%10
#     bin= bin//10
#     rev =rev*10+r
# print("binary reverse value", rev)