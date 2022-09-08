n = int(input())
heights = list(map(int, input().split()))

sub = abs(heights[0] - heights[-1])
index = [1,len(heights)]

for i in range (0,len(heights)-1):
    test = abs(heights[i] - heights[i+1])
    if test < sub:
        sub = test
        index = [i+1,i+2]
    else :
        pass

for j in index:
    print(j, end=" ")
