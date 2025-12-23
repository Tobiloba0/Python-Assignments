def convert_to_list(card_number):
    return [int(digit) for digit in card_number]

def digit_doubling(card_array):
    total = 0
    for index in range(len(card_array) - 2, -1, -2):
        number = card_array[index] * 2
        if number > 9:
            number -= 9
        total += number
    return total

def odd_number_sum(card_array):
    total = 0
    for index in range(len(card_array) - 1, -1, -2):
        total += card_array[index]
    return total

def is_valid(card_array):
    total = odd_number_sum(card_array) + digit_doubling(card_array)
    return total % 10 == 0

def credit_card_type(card_array):
    if card_array[0] == 4:
        return "Visa Card"
    if card_array[0] == 5:
        return "Master Card"
    if card_array[0] == 3 and card_array[1] == 7:
        return "American Express Card"
    if card_array[0] == 6:
        return "Discover Card"
    return "Unknown Card Type"

card_number = input("Enter your Credit Card Number: ")
card_array = convert_to_list(card_number)

print("Credit Card Type:", credit_card_type(card_array))
print("Credit Card Number:", card_number)
print("Credit Card Digit Length:", len(card_array))
print("Credit Card validity status:", "Valid" if is_valid(card_array) else "Invalid")




