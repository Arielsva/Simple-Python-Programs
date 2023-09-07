text = input("Insira texto a ser criptografado: ")
while True:
    value = input("Insira um número de 1 a 25\n>> ")
    if value.isalnum() and value in [str(num) for num in range(1, 26)]:
        value = int(value)
        break
    else:
        print("Digite um valor válido!\n")
# Other way:
"""
while True:
    try:
        value = int(input("Insira um número de 1 a 25\n>> "))
        if value in range(1, 26):
            break
    except ValueError:
        print("Digite um número válido!\n")
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ""

for char in text:
    if char.isalpha():
        index_ = alphabet.index(char.lower())
        index_ = value + index_
        if index_ >= len(alphabet):
            while index_ >= len(alphabet):
                index_ = abs(len(alphabet) - (index_))
        print(char)
        encrypted_text += alphabet[index_].upper()
    else:
        encrypted_text += char

print(encrypted_text)
                        

"""
# Sample Solution

# Input the text you want to encrypt.
text = input("Enter message: ")

# Enter a valid shift value (repeat until it succeeds).
shift = 0

while shift == 0:
    try:    
        shift = int(input("Enter the cipher shift value (1..25): "))
        if shift not in range(1,26):
        	raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Incorrect shift value!")

cipher = ''

for char in text:
    # Is it a letter?
    if char.isalpha():
        # Shift its code.
        code = ord(char) + shift
        # Find the code of the first letter (upper- or lower-case)
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # Make correction.
        code -= first
        code %= 26
        # Append the encoded character to the message.
        cipher += chr(first + code)
    else:
        # Append the original character to the message.
        cipher += char

print(cipher)
"""