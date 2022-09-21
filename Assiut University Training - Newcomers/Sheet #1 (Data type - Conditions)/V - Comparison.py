x = input()

if '>' in x:
    x=x.split(">")
    if int(x[0]) > int(x[1]):
        print("Right")
    else:
        print("Wrong")

elif '<' in x:
    x=x.split("<")
    if int(x[0]) <  int(x[1]):
        print("Right")
    else:
        print("Wrong")

else:
    x=x.split("=")
    if int(x[0]) ==  int(x[1]):
        print("Right")
    else:
        print("Wrong")
