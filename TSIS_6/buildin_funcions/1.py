def multiply(numbers):
    s = 1
    for i in numbers:
        s*=int(i)
        
    print(s)


inp = input("print numbers: ")
arr = inp.split()
listt = []
for i in range (len(arr)):
    listt.append(arr[i])
    
multiply(listt)