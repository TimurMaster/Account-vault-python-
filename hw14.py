n = int(input())
if(n <= 1000):
    print(n+2-(n%2))
else:
    print("Ошибка,число превысило 1000")