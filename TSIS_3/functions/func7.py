def has33(x):
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            return True
        
    return False
    
    
    
inp = input("")
arr = inp.split()
if has33(arr) == True:
    print("True")
else:
    print("False")