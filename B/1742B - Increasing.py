t = int(input())

for i in range(t):
    length = int(input())
    lst = list(map(int,input().split()))

    if length == len(set(lst)):
        print('YES')
    else:
        print("NO")
