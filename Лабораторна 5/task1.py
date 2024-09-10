N = int(input("Введіть довжину масиву N: "))
print("Введіть елементи масиву: ")

array = [int(input(f"Введіть елемент {i}: ")) for i in range(N)]

negative_elements = [x for x in array if x < 0]

if negative_elements:
    average_negative = sum(negative_elements) / len(negative_elements)
    print("Середнє арифметичне від’ємних елементів:", average_negative)
else:
    print("У масиві немає від’ємних елементів.")
