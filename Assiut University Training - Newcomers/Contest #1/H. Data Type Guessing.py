n, k, a= map(int,input().split())

result = (n*k)/a
result_int = int(result)
subtraction = result - result_int

if subtraction > 0:
    print("double")

elif result_int <= 2147483647:
    print('int')

else:
    print("long long")
