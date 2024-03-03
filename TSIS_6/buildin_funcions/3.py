def polindrome(word):
    check = ""
    for i in range(len(word)-1,-1,-1):
        check+=word[i]
        
    if word == check:
        print("Polindrome")
    else:
        print("Not")






s = str(input(""))
polindrome(s)