def unique(x):
    uniq = []
    if x[0] != x[1]:
        uniq.append(x[0])
    for i in range (1,len(x)-1):
        if x[i] != x[i+1] and x[i-1] != x[i]:
            uniq.append(x[i])
    if x[len(x)-1] != x[len(x) - 2]:
        uniq.append(x[len(x)-1])
            
    print (uniq)
    
    
    
    
inp = input("")
arr = inp.split()
unique(arr)