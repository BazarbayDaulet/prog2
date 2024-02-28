import re

x = re.compile(r'[a-z]+_[a-z]+')

s = input("Enter a string: ")

matches = x.findall(s)
print(f'Sequences of lowercase letters joined with an underscore: {matches}')
