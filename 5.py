start = 1
finish = 100
count = 0

while True:
    chislo = (start+finish)//2
    
    print("Твое число равно, больше или меньше, чем число "+str(chislo)+" ?")
    
    answer = int(input("Введите ответ: "))
    
    if answer == 1:
        print("Ваше число: "+str(chislo))
        break
    
    if answer == 2:
        start = chislo
    
    if answer == 3:
        finish = chislo
        
    count +=1
    
print(count)