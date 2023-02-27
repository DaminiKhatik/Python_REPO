#Matching the beginning of a string
import re
pattern = r"123" 
string = "123zzb"
match = re.match(pattern, string) 
print(match)


# Searching
pattern = r"(your base)" 
sentence = "All your base are belong to us."
match = re.search(pattern, sentence) 
match.group(1) 
print(match)


# Precompiled patterns
import re
precompiled_pattern = re.compile(r"(.*\d+)")
matches = precompiled_pattern.match("The answer is 41!")
print(matches.group(1)) 

# Flags
m = re.search("b", "ABC", flags=re.IGNORECASE) 
m.group() 
print(m)

m = re.search("a.b", "A\nBC", flags=re.IGNORECASE|re.DOTALL)
m.group() 
print(m)

m = re.search("b", "AB\nC", flags=re.MULTILINE) 
print(m)

#Replacing

a=re.sub(r"t[0-9][0-9]", "foo", "my name t13 is t44 what t99 ever t44") 
print(a)