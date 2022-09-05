t = int(input())
results = []

for i in range(t):
      ticket = list(input())

      if int(ticket[0])+int(ticket[1])+int(ticket[2]) == int(ticket[3])+int(ticket[4])+int(ticket[5]):
            results.append("YES")

      else :
            results.append("NO")

for result in results:
      print(result)
