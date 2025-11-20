
total_sum = 0
product = 1
smallest = 0
largest = 0



for integers in range(4):
    number = int(input(f"Enter integer{integers + 1}: "))
    
    total_sum += number
    product *= number
    if number < smallest:
        smallest = number

    if number > largest:
        largest = number
    
    

average = total_sum / integers
print(total_sum)

print(product)

print(average)
print(smallest)
print(largest)




