a = int(input("Введіть a:"))

while (a <= 0):
    print("a приймає тільки додатні значення!")
    a = int(input("Введіть a:"))

b = int(input("Введіть b:"))

while (b <= 0):
    print("b приймає тільки додатні значення!")
    b = int(input("Введіть b:"))

x = 0

if a < b:
    x = a/b + 5
elif a == b:
    x = -5
else :
    x = (a*a-b)/b

print(f"X = {x}")

