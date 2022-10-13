t = int(input())

for case in range(t):
    size_1, size_2 = input().split()

    if len(size_1) == len(size_2):
        if size_1[-1] == size_2[-1]:
            print("=")

        elif size_1[-1] > size_2[-1]:
            print("<")

        else:
            print(">")


    else:
        if size_1[-1] > size_2[-1]:
            print("<")

        elif size_1[-1] < size_2[-1]:
            print(">")

        else:
            if size_1[-1] == "S":
                if len(size_1) < len(size_2):
                    print(">")
                else:
                    print("<")
            else:
                if len(size_1) < len(size_2):
                    print("<")
                else:
                    print(">")
