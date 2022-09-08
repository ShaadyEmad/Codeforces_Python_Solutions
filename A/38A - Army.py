n = int(input())
years = list(map(int, input().split()))
ranks = list(map(int, input().split()))

start_rank = ranks[0]
target_rank = ranks[1]
sum = 0

for i in range(start_rank, target_rank):
    sum += years[i-1]
    
print(sum)
