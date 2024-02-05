def filter(x):
    if int(x) < 2:
        return False
    
    for i in range(2, int(int(x)**0.5)+1):
        if int(x) % i == 0:
            return False
    return True
    
inp = input("")
array = inp.split()
for i in range(len(array)):
    if filter(array[i]) == True:
        print(array[i], end=" ")

    
