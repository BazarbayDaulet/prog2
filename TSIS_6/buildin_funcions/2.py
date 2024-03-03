def calcualte(word):
    Up = 0
    low = 0
    for i in range(len(word)):
        if word[i] >= 'A' and word[i] <= 'Z':
            Up+=1
        elif word[i] >= 'a' and word[i] <= 'z':
            low+=1
            
    print (Up, low)


s = str(input(""))
calcualte(s)