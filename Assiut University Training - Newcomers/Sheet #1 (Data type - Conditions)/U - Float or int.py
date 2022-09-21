n = input()

if float(n).is_integer():
    n = n.split(".")
    print("int", end=" ")
    print(n[0])

else:
    n = n.split(".")
    print("float",end=" ")
    print(n[0],end=" ")
    print(f"0.{n[1]}")
