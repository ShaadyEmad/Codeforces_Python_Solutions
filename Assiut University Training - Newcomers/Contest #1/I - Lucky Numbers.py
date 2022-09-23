n = input()
n = [x for x in n]

if (int(n[1]) == 0) or (int(n[0]) % int(n[1]) == 0) or (int(n[1]) % int(n[0]) == 0):
    print('YES')

else:
    print('NO')
