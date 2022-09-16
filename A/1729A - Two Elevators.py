t = int(input())

for i in range(t):
    a, b, c = [int(x) for x in input().split()]
    distance_a = abs(a-1)
    distance_b = abs(b-c) + abs(c-1)

    if distance_b > distance_a:
        print("1")

    elif distance_b < distance_a:
        print("2")

    else:
        print("3")
