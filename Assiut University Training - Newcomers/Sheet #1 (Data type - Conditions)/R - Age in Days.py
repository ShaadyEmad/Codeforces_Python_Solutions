n = int(input())
years = 0
months = 0
days = 0

while n >= 365:
    n -= 365
    years +=1

while n >= 30:
    n -= 30
    months += 1

while n >= 1:
    n -= 1
    days += 1

print(f"{years} years")
print(f"{months} months")
print(f"{days} days")
