def find_subsequence(lst, subsequence):
    n, m = len(lst), len(subsequence)
    
    for i in range(n - m + 1):
        if lst[i:i + m] == subsequence:
            return True 
    return False 


lst = list(map(int, input("Введіть основний список: ").split()))
    
subsequence = list(map(int, input("Введіть шуканий список: ").split()))
    
if find_subsequence(lst, subsequence):
    print("Підпослідовність знайдена!")
else:
    print("Підпослідовність не знайдена.")

