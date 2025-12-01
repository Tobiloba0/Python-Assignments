

def greatest_divisor(number1, number2):
    gcd = 1

    # Loop through all possible divisors
    for count in range(1, min(number1, number2) + 1):
        if number1 % count == 0 and number2 % count == 0:
            gcd = count

    return gcd


number1 = 12
number2 = 18

print(greatest_divisor(number1, number2))

