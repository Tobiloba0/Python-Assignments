
def greatest_divisor(number1, number2):
    gcd = 1
    for count in range(1, min(number1, number2) + 1):
        if number1 % count == 0 and number2 % count == 0:
            gcd = count
    return gcd


def lowest_multiple(number1, number2):
    gcd = greatest_divisor(number1, number2)
    lcm = (number1 * number2) // gcd   # integer division
    return lcm


number1 = 5
number2 = 10

print(lowest_multiple(number1, number2))

