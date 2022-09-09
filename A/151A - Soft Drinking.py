import math

friends, bottles, milliliters, limes, slices, salt, nl, np = [int(x) for x in input().split()]

total_drinks = (bottles * milliliters)/nl
total_slices = limes * slices
total_salt = salt/np

toast = math.floor(min(total_slices,total_drinks,total_salt)/friends)

print(toast)
