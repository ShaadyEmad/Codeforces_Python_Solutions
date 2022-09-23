discount, price_after = map(int,input().split())
discount = 100 - discount
price_before = round(100*price_after/discount,2)
print("{:.2f}".format(price_before))
