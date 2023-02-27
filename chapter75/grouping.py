
import re
sentence = "This is a phone number 672-123-456-9910"
pattern = r".*(phone).*?([\d-]+)"
match = re.match(pattern, sentence)
match.groups() 
print(match)