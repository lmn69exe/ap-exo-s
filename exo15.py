vowels = ['a', 'e', 'o']

string = input("Insert a string: ")

for vowel in vowels:
    if vowel in string:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")
