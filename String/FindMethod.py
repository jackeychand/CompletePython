# find method is use to find the matching charachter or string
s = "Hi Jackey How are you"
print(s.find('J'))
print(s.find('z'))
print(s.find('J',4))
print(s.find('o',0,len(s)))
print(s.find('o',12,len(s)))


#rfind() methos is smilar to find() but it match from right to lefthand side
print(s.rfind('r'))
print(s.rfind('r',0,14))
print(s.rfind('o',0,14))


#index

print(s.index('y'))
print(s.index('H',0,len(s)))
print(s.index('H',1,len(s)))

#rindex

print(s.rindex('H'))


#count

print(s.count('o'))
print(s.count('o',12,len(s)))
