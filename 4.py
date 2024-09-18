n = int(input("Введите число: "))

for i in range(n):
    for j in range(n, n - i - 1, -1):
        print(j, end="")
    
    thk_count = (n - i - 1) * 2
    for z in range(thk_count):
        print(".", end="")
    
    for k in range(n - i, n + 1):
        print(k, end="")
        
    print()
