text = input("Input the word: ").lower().replace(' ', '')

print(text)

if text == text[::-1] and len(text) > 1:
    print("It's a palindrome")
else:
    print("It's not a palindrome")

# Ten animals I slam in a net

# Eleven animals I slam in a net