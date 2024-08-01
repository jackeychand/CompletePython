s = "python"

print(s.ljust(10,))
print(s.ljust(10,'@'))
print(s.rjust(10,'@'))
print(s.center(10,'@'))
print(s.center(4))

#strip is use to remove space by default
s1 = "    jackey     @"
print(s1)
print(s1.lstrip())
print(s1.rstrip())
print(s1.strip(' @'))