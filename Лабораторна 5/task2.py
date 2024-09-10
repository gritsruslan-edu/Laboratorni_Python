n = 7

array = [[(i + j >= n - 1)*(i + j - (n - 2)) for i in range(n)] for j in range(n)]


for row in array:
    print(*row)
