discount, price_afer = map(int,input().split())
discount = 100 - discount
price_before = round(100*price_afer/discount,2)
print("{:.2f}".format(price_before))
