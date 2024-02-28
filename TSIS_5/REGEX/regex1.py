import re


x = re.compile(r'a*b*')



s = input("Enter a string: ")


if x.fullmatch(s):
    print(f'The string "{s}" matches the pattern.')
else:
    print(f'The string "{s}" does not match the pattern.')
