n = int(input())
num = list(map(int,input()))


# check that the first half does not equal the sum of digits in the second half
if sum(num[:int(n/2)]) == sum(num[int(n/2):]):
    condition1 = True
else:
    condition1 = False


# check that it's lucky number
for i in num:
    if i == 4 or i == 7:
        condition2 = True
        pass
    else:
        condition2 = False
        break


if condition1 and condition2:
    print("YES")
else :
    print("NO")
