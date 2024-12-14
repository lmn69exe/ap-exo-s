name = input("Please enter your name : ")

if name == "VIP":
    print("Enjoy the show for free!")
else:
    numTic = int(input("How many tickets would you like to buy : "))
    cost = numTic * 15.50
    print(f"The total cost is {cost}")
    print("Enjoy the show!")