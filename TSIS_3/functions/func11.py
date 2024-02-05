def polindrome(s):
    rev = s[::-1]
    if s == rev:
        print("polindrome")
    else:
        print("not polindrome")
    
    
string = input("print word")
polindrome(string)