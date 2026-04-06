# Fibonacci sequence (first 20 numbers)

first = 1
second = 1

print(first)
print(second)

for i in range(18):
    next_num = first + second
    print(next_num)
    first = second
    second = next_num