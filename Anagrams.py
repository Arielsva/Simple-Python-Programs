""" from random import shuffle

first_word = list(input("Input the first word: ").lower().replace(' ', ''))
second_word = input("Input the second word: ").lower().replace(' ', '')
y = 1

for x in range(1, len(first_word) + 1):
    y *= x

for x in range(1, y + 1):
    t = list(first_word)
    shuffle(t)
    if second_word == ''.join(t):
        print("Anagrams")
        break
else:
    print("Not anagrams") """



first_word = sorted(input("Input the first word: ").lower().replace(' ', ''))
second_word = sorted(input("Input the second word: ").lower().replace(' ', ''))

if len(first_word) > 1 and len(second_word) > 1 and first_word == second_word:
    print("Anagrams")
else:
    print("Not anagrams")