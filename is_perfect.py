
def is_perfect(number):
    perfect_number = 0

   
    for count in range(1, number):
        if number % count == 0:
            perfect_number += count

    # if the sum of the factors equals the number, it's perfect
    return perfect_number == number



number = 28

print(is_perfect(number))

