import re

x = re.compile(r'[A-Z][a-z]+')

s = input("Enter a string: ")

matches = x.findall(s)
print(f'Sequences of one uppercase letter followed by lowercase letters: {matches}')
