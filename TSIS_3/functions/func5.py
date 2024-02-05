from itertools import permutations

def ipermutations(string):
    
    all = permutations(string)

    for perm in all:
        print(''.join(perm))


inp = input("Enter a string: ")


ipermutations(inp)
