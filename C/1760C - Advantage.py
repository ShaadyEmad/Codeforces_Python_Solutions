n = int(input())

for i in range (n):
    length = int(input())
    lst = list(map(int, input().split()))
    max1 = sorted(lst)[-1]
    max2 = sorted(lst)[-2]
    for j in lst:
        if j == max1:
            print(j-max2,end=" ")
        else:
            print(j-max1,end=" ")
    print()
