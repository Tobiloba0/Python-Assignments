
def is_Perfect(numbers):
    result = []
    for num in numbers:
        isPerfectSquare = False

        if num >= 0:
            count = 0
            while count * count <= num:
                if count * count == num:
                    isPerfectSquare = True
                    break
                count += 1
        result.append(isPerfectSquare)

    return result                

#main part
if _name_ == "_main_": 
numbers = [4, 9, 25, 49]
answer = isPerfect(numbers)

for value in answer:
print(value, end= " ")
    







