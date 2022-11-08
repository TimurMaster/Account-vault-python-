n = int(input())
if (n<= 0 or n>100):
    print("Превышен лимит, введите число от 1 до N")
    exit()
else:
    print(2 ** n)