import statistics

grade = [4, 5, 8, 2, 5]

mean = statistics.mean(grade)
mode = statistics.mode(grade)
median = statistics.median(grade)
arranged = sorted(grade)

print(mean)
print(mode)
print(median)
print(arranged)
