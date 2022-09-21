x = input().split(" ")

if x[1] == '+':
    if (int(x[0]) + int(x[2])) == int(x[4]):
        print("Yes")
    else:
        print(int(x[0]) + int(x[2]))

elif x[1] == '-':
    if (int(x[0]) - int(x[2])) == int(x[4]):
        print("Yes")
    else:
        print(int(x[0]) - int(x[2]))

else:
    if (int(x[0]) * int(x[2])) == int(x[4]):
        print("Yes")
    else:
        print(int(x[0]) * int(x[2]))
