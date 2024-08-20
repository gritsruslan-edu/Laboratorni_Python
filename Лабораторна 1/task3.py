N = int(input("Введіть N:"))

while N <= 1 or N >= 9:
    print("N повинно задовольняти 1<N<9!")
    N = int(input("Введіть N:"))

for i in range(1, N + 1):
    currentRow = ""
    for j in range(1, i + 1):
        currentRow += str(j) + " "
    print(currentRow)
