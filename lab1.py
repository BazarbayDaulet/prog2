#syntax 

print("Hello world")


if 5 > 2:
    print("YES")








    
#comments
1

#This is a comment



2

"""This is a comment
written in 
more than just one line"""









#variables
1
carname = "Volvo"

2
x = 50

3
x = 5
y = 10
print(x+ y)

4
x= 5
y = 10
z = x + y
print(z)

5
x,y,z =  "Orange", "Banana", "Cherry"

6
x=y=z="orange"

7
def myfunc():
  
  global x
  x = "fantastic"
  





#data types
1
x = 5
print(type(x))


int

2
x = "Hello World"
print(type(x))

str

3
x = 20.5
print(type(x))

float

4
x = ["apple", "banana", "cherry"]
print(type(x))

list

5
x = ("apple", "banana", "cherry")
print(type(x))

tuple

6

x = {"name" : "John", "age" : 36}
print(type(x))

dict

7
x = True
print(type(x))

bool

8






#numbers
1
x = 5
x = int(x)

2
x = 5.5
x = int(x)

3
x = 5
x = complex(x)







#strings
1
x = "Hello world"
print(len(x))

2
txt = "Hello World"
x = txt[0]

3
txt = "Hello World"
x = txt[2:5]


4
txt = " Hello World "
x = txt.strip()

5
txt = "Hello World"
txt = txt.upper()


6
txt = "Hello World"
txt = txt.upper()

7
txt = "Hello World"
txt = txt.replace('H' , 'J')

8
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


    
    