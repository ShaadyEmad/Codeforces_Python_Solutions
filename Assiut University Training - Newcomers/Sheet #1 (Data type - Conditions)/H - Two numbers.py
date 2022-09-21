import math

a, b = map(int,input().split())
result = a/b

# i made this function because the Built-in function round() round 2.5 to 2 not 3
def round_up(result):
  f = math.floor(result)
  return f if result - f < 0.5 else f+1

print(f"floor {a} / {b} = {math.floor(result)}")
print(f"ceil {a} / {b} = {math.ceil(result)}")
print(f"round {a} / {b} = {round_up(result)}")
