    n = int(input())
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
     
    for i in range (n):
        l = int(input())
        s = input()
        print(alphabets.index(max(s))+1)
