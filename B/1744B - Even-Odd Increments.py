t = int(input())

for case in range(t):
    length, queries_num = map(int,input().split())
    lst = list(map(int,input().split()))

    evens = odds = 0
    lst_sum = sum(lst)

    for num in lst:
        if num % 2 ==0:
            evens+=1
        else:
            odds+=1

    for i in range(queries_num):
        x_type, addition = map(int, input().split())

        if x_type == 0:
            lst_sum += addition * evens
            if addition%2 != 0 :
                odds += evens
                evens = 0

        else:
            lst_sum += addition * odds
            if addition%2 != 0:
                evens += odds
                odds = 0

        print(lst_sum)
