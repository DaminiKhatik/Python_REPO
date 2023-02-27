import re
match = re.search(r'[b]', 'a[b]c')
match.group() 
print(match)