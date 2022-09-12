q = int(input())
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
results = []

for i in range(q):
    n = int(input()) # the length of the given code.
    t = input() # code
    t = [int(d) for d in str(t)]
    count =0

    while True:
        if len(t) >= 4:
            if t[2] == 0:
                if t[3]== 0:
                    x = t[0]
                    result = alphabet[x - 1]
                    results.append(result)
                    t.pop(0)
                    continue

                elif t[3] != 0:
                    x = int(str(t[0]) + str(t[1]))
                    result = alphabet[x - 1]
                    results.append(result)
                    t.pop(0)
                    t.pop(0)
                    t.pop(0)
                    continue

            else:
                x = t[0]
                result = alphabet[x - 1]
                results.append(result)
                t.pop(0)
                continue


        if len(t) == 3:
            if t[2] == 0:
                x = int(str(t[0]) + str(t[1]))
                result = alphabet[x - 1]
                results.append(result)
                t.pop(0)
                t.pop(0)
                t.pop(0)
                continue
            else:
                x = t[0]
                result = alphabet[x - 1]
                results.append(result)
                t.pop(0)
                continue


        if (len(t) == 2) or (len(t) == 1):
            x = t[0]
            result = alphabet[x - 1]
            results.append(result)
            t.pop(0)
            continue
        else:
            print(''.join(results))
            results.clear()
            break
