price= float(input("Put the price"))
if price < 100:
    discount= price * 0.02
    final_price= price * discount
elif price >= 100:
    discount= price * 0.1
    final_price= price - discount
print(f"Your final price is {final_price}")