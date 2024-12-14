price = float(input("Total amount: "))
num_items = int(input("Number of items: "))
day = input("Day of the week: ")

if day in ['Saturday', 'Sunday']:
    rate = .2
else:
    rate = .1

if num_items > 5:
    rate += .05

new_price = price - (price*rate)

print(f"Total price after discount: {new_price}")