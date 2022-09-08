string_1 = input().lower()
string_2 = input().lower()

count = 0

for i in range(0,len(string_1)):
    if string_1[i] == string_2[i]:
        count+=1
        if count == len(string_1):
            print("0")
            break

    elif ord(string_1[i]) > ord(string_2[i]):
        print("1")
        break

    else:
        print("-1")
        break
