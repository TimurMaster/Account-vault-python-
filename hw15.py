n = int(input())
if n > 1000:
    print("Число превышает 1000")
    exit()
else:
    n = str(n) * 100
    print(n , "- возводим это число в квадрат.")
    n = int(n) ** 2
    print(n , " - результат.")