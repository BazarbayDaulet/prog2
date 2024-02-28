import re

x = re.compile(r'ab{2,3}')

s = input("Enter a string: ")

if x.search(s):
    print(f'The string "{s}" matches the pattern.')
else:
    print(f'The string "{s}" does not match the pattern.')
