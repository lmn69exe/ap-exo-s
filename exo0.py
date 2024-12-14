numPpl = int(input("How many people need a ride : "))
numFit = int(input("How many people can fit in one taxi : "))

numTaxi = numPpl // numFit
numLeft = numPpl % numFit

if numPpl % 2 == 0:
    print(f"The number of taxi's needed is {numTaxi}")
else:
    print(f"The number of taxis needed is {numTaxi + 1}")
    print(f"The last taxi wil hold {numLeft}");