t = int(input())

for i in range(t):
    lst1= list(map(int, input().split()))
    lst2= list(map(int, input().split()))

    def rotate(lst1,lst2):
        temp = lst2[1]
        lst2[1] = lst1[1]
        lst1[1] = lst1[0]
        lst1[0] = lst2[0]
        lst2[0] = temp
        return lst1,lst2

    if (lst1[0] < lst1[1]) and (lst1[0] < lst2[0]) and (lst1[1] < lst2[1] ) and (lst2[0]  < lst2[1] ):
        print('YES')

    else:
        i = 0
        while True:
            if i != 3:
                lst1,lst2 = rotate(lst1,lst2)
                i +=1
                if (lst1[0] < lst1[1]) and (lst1[0] < lst2[0]) and (lst1[1] < lst2[1] ) and (lst2[0]  < lst2[1] ):
                    print('YES')
                    break
            else:
                print("NO")
                break
