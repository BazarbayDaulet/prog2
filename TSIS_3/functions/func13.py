import random

def play(x):
    print("Hello, what is your name?")
    name = input("")
    print("Well," + name + ", I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    pop = 1
    while 1:
        wr = int(input(""))
        
        if wr > x:
            print("Your guess is too high")
            print("Take a guess.")
            pop += 1
        elif wr < x:
            print("Your guess is too low")
            print("Take a guess.")
            pop += 1
        else:
            print("Good job, KBTU! You guessed my number in " + str(pop) + " guesses!")
            break

v = random.randint(1, 20)
play(v)
