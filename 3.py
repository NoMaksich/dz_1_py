import math

count = int(input("Количество чисел: "))
easy_count = 0

for j in range(count):
    chislo = int(input("Введите число: "))
    
    if chislo < 2:
        continue
    for i in range(2, int(math.sqrt(chislo)) + 1):
        if chislo % i == 0:
            break 
    else:
        easy_count += 1

print("Количество простых чисел в последовательности: " + str(easy_count))
