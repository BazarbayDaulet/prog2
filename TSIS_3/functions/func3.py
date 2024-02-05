def solve(numheads, numlegs):
    y = (int(numlegs) / 2) - int(numheads)
    x = (int(numheads) - int(y))
    print("chickens: ", x)
    print("rabbits: ", y)
    
    
head = int(input("heads: "))
leg= int(input("legs: "))
solve(head, leg)