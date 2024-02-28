import re

input_string = input("Enter a string: ")
result_string = re.sub(r'(?<=[a-z])([A-Z])', r' \1', input_string)
print(f'The modified string is: {result_string}')
