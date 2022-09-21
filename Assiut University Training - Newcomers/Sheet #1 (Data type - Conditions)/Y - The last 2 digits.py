a, b, c,d = map(int, input().split())

multiplication = a*b*c*d
lst= [int(d) for d in str(multiplication)]

for i in lst[-2:]:
    print(i, end="")
