t = int(input())

for case in range(t):
    n = int(input())
    line1 = list(input())
    line2 = list(input())

    # replace every 'G' with 'B'
    for i in range (n):
        if line1[i] == 'G':
            line1[i] = 'B'

        if line2[i] == 'G':
            line2[i] ='B'


    for j in range(n):
        if line1[j] == line2[j]:
            condition = True
        else:
            condition = False
            break

    # check condition
    if condition:
        print("YES")
    else:
        print("NO")
