n = 7

array = [[(i + j >= n - 1)*(i + j - (n - 2)) for i in range(n)] for j in range(n)]


for row in array:
    print(*row)


# OLD =============


# array = [[0 for _ in range(n)] for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         if i + j < n - 1:
#             array[i][j] = 0
#         else:
#             array[i][j] = i + j - (n - 2)
