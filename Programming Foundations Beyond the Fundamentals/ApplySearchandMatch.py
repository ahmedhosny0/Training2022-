import re
a ='123'
b='1243-456'
c='9949-33-2242'
ch=r'\d{3}'
print(re.search(ch,a))
print(re.search(ch,b))
print(re.search(ch,c))