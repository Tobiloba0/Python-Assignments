import random

numbers = []

for _ in range(10):
    numbers.append(random.randint(1, 50))
print(numbers)

list_length = 0
for _ in numbers:
    list_length +=1
print(list_length)


sum_total = 0
index = 0

for value in numbers:
    if index % 2 == 0:
        sum_total += value
    index +=1
print(sum_total)


sum_odd_total = 0
index = 0

for value in numbers:
    if index % 2 == 1:
        sum_odd_total += value
    index +=1
print(sum_odd_total)


multiplied_third = 1
index = 0

for value in numbers:
    if index % 3 == 2:
        multiplied_third *= value
    index+=1
print(multiplied_third)

#calculating average of all element

total_value= 0
count = 0
for value in numbers:
    total_value += value
    count +=1
average = total_value / count
print(average)

# getting the largest element in the list 

largest = numbers[0]
for value in numbers:
    if value > largest:
        largest = value
print(largest)

#getting the smallest value

smallest = numbers[0]
for value in numbers:
    if value < smallest:
        smallest = value
print(smallest)    
    
    


