import math

t = int(input())
for case in range(t):
    num = int(input())
    digits = list(map(int, input().split()))
    
    minimum_digit_index = digits.index(min(digits))
    digits[minimum_digit_index] += 1
    print(math.prod(digits))
