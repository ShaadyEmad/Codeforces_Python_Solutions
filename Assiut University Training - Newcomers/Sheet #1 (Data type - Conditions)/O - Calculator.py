import math

x = input()

if '+' in x:
    x=x.split("+")
    print(int(x[0]) + int(x[1]))

elif '-' in x:
    x=x.split("-")
    print(int(x[0]) - int(x[1]))

elif '*' in x:
    x = x.split("*")
    print(int(x[0]) * int(x[1]))

elif '/' in x:
    x = x.split("/")
    print(math.floor(int(x[0]) / int(x[1])))
