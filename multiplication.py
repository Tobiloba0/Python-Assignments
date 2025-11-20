print("number\tsquare\tcube")
for number in range(0, 6):
    square = number * number
    cube = square * number
    print(f"{number:>6}\t{square:>6}\t{cube:>4}")
