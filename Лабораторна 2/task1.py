from mod import calculate_distance

def expression (m):
    return 1/((m+2)**0.5)

m = float(input("Введіть число m: "))

while m == 0:
    print("Число m повинно бути відмінним від нуля!")
    m = float(input("Введіть число m ще раз: "))

print(f"Z = {expression(m)}")


n = int(input("Введіть число днів, які пробіг спортсмен: "))

while n < 1:
    print("Кількість днів повинна бути 1 або більше!")
    n = int(input("Введіть кількість днів ще раз: "))

distance = calculate_distance(n)

print(f"За всі дні спортсмен пробіг {distance} кілометрів.")
