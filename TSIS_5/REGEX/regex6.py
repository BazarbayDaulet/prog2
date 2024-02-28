import re

s = input("Enter a string: ")
res = re.sub(r'[ ,.]', ':', s)
print(f'The modified string is: {res}')
