a, b, x,y = map(int, input().split())

if max(a,x) > min(b,y):
    print('-1')

else:
    print(f'{max(a,x)} {min(b,y)}')
