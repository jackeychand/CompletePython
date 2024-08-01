s = 'This is my world'

print(s.startswith('Th'))
print(s.startswith('This'))
print(s.startswith('is'))
print(s.startswith('is',5))


print(s.endswith('world'))
print(s.endswith('my'))
print(s.endswith('my',0,10))


print(s.partition('is'))
print(s.partition(' '))

print(s.rpartition('is'))
print(s.rpartition(' '))


print(s.removeprefix('This'))
print(s.removeprefix('is'))

print(s.removesuffix('This'))
print(s.removesuffix('world'))
