import time
import math

def root(number, milliseconds):
    time.sleep(milliseconds / 1000.0)  
    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")


number = int(input("Enter the number: "))
milliseconds = int(input("Enter the delay in milliseconds: "))


root(number, milliseconds)
