date = input("Input your birthday date in YYYYMMDD format: ")

if date.isalnum() and len(date) == 8:
    while len(date) > 1:
        digit = 0
        
        # for num in date:
        #     date = str(digit + int(num))
        #     digit = int(date)

        for num in date:
            digit += int(num)
        date = str(digit)

    print(date)
else:
    print("Invalid")