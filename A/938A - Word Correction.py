n = int(input())
s = list(input())

vowels = ['a', 'e', 'i', 'o', 'u', 'y']
i = 0

while i+1 < len(s):
    if (s[i] in vowels) and (s[i+1] in vowels):
        del s[i+1]

    else:
        i +=1

print("".join(s))
