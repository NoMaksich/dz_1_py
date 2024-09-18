a = int(input("Введите сторону 1: "))
b = int(input("Введите сторону 2: "))
c = int(input("Введите сторону 3: "))

if a > b+c or b > a+c or c > a+b:
    print("Треугольника с такими сторонами не существует")
    exit()

if a!=b and a!=c and c!=b:
    print("Треугольник разносторонний")
elif a==b and a==c and c==b:
    print("Треугольник равносторонний")
else:
    print("Треугольник равнобедренный")
    
