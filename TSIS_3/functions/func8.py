def spy_game(x):
    arr2= []
    for i in range(len(arr)):
        if x[i] == "0" or x[i] == "7":
            arr2.append(x[i])
        
    for i in range(len(arr2)-2):
        if arr2[i] == "0" and arr2[i + 1] == "0" and arr2[i + 2] == "7":
            print("True")
            return 0
    print("False")
        
    
    
    
    
    
inp = input("")
arr = inp.split()
spy_game(arr)
