import re

s = input("Enter a string: ")
result_list = re.findall('[A-Z][^A-Z]*', s)
print(f'The split string at uppercase letters: {result_list}')
