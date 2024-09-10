def insert_elem(lst: list, index: int, element):
    if index == len(lst):
        lst.append(element)
    else:
        lst[:] = lst[:index] + [element] + lst[index:]

lst = list(map(int, input("Введіть список: ").split()))

print(f"Оригінальний список: {lst}")

index = int(input('Введіть індекс нового елемента: : '))

while(index > len(lst) or index < 0):
    print("Некоректний індекс!")
    index = int(input("Спробуйте ввести ще раз : "))

new_elem = int(input("Введіть новий елемент: "))

insert_elem(lst, index, new_elem)

print(f"Оновлений список: {lst}")
