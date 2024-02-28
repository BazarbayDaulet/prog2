import re
s = input("Enter a snake case string: ")
words = s.split('_')
camel_case_string = words[0] + ''.join(word.capitalize() for word in words[1:])
print(f'The camel case string is: {camel_case_string}')
