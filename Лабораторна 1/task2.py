first = 0
second = 1

previous = first
current = second

print(first)
print(second)

fib_number = 2
sum = first + second

for fib_number in range(2, 8):
    previous, current = current, previous + current
    sum = sum + current
    print(current)

print(f"Сумма: {sum}")