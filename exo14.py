word = input("Insert a word: ")

padding = 30 - len(word) - 2
left_padd = padding // 2
right_padd = padding - left_padd

print("*"*30)
print("*" + " "*left_padd + word + " "*right_padd + "*")
print("*"*30)