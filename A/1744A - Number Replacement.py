t = int(input())

for case in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    s = input()
    d={}
    output = 'YES'

    for i in range(n):
         if lst[i] in d:
             if d[lst[i]] != s[i]:
                 output = 'NO'
                 break
         else:
             d[lst[i]] = s[i]

    print(output)
