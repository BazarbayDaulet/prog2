import re


input_string = input("Введите строку в стиле camel case: ")


snake_case_string = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', input_string).lower()


print(f'Строка в стиле "snake case": {snake_case_string}')
