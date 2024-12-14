print("Runner 1:")
first_name = input("Name: ")
first_time = float(input("Time (in seconds): "))

print("Runner 2:")
second_name = input("Name: ")
second_time = float(input("Time (in seconds): "))

if first_time > second_time:
    print(f"The faster runner is {second_name}")
elif second_time > first_time:
    print(f"The faster runner is {first_name}")
else:
    print(f"{first_name} and {second_name} have the same time!")