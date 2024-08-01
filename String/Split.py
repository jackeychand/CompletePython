s = 'Where are you going'
s1 = 'i,am,going,to,school'
s2 = 'can-i-call-you'
 
print(s.split()) 
print(s1.split(',')) 
print(s1.split('t')) 
print(s2.split('-',2))
print(s2.rsplit('-',2))

s3 = 'aaa\nbbb\n\tccc\nddd'
print(s3.splitlines())
print(s3.splitlines(keepends=True))
print(s3.split())