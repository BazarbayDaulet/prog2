def reverse(word):
    for i in range(len(word)-1, -1, -1):
        print(word[i], end=" ")    
    
inp = input("")
sent = inp.split()
reverse(sent)
