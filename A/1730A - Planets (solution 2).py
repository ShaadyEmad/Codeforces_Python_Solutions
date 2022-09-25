t=int(input())

for i in range(t):

    n,c=map(int, input().split())
    l=list(map(int,input().split()))
    cost=0

    for j in set(l):
        cost=cost+min(l.count(j),c)
        
    print(cost)
