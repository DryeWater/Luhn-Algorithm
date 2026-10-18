def luhn(number):
    total = 0
    for i, digit in enumerate(reversed(number)):
        digit = int(digit)

        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                total += (digit - 9)
                print(total)
            else:
                total += digit
                print(total)
        else:
            total += digit
            print(total)
    print(total)
    return total

credit = input("enter your credit number: ").replace(" ", "")
y = luhn(credit)
if y % 10 == 0:
    print("VALID NUMBER")
else:
    print("NO")
