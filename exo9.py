cities = []

while True:
    city = input("Insert a city name (type 'stop' to stop haha): ")

    if city == 'stop':
        break
    
    population = len(city)*1000000
    cities.append((city, population))

cities.sort()

for city, population in cities:
    print(f"The city '{city}' has {len(city)} letters, so it's population is {population}")