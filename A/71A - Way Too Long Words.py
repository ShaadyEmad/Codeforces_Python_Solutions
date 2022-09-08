n = int(input())

for i in range (n):
    word = list(input())
    if len(word) > 10 :
        print(word[0],end="")
        print(str(len(word)-2), end="")
        print(word[-1])

    else:
        print("".join(word))
