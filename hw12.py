number = int(input())
if number < -1000 or number > 1000:
    print("Ошибка, введите другое число")
else:
    print("The next number for the number",number,"is",number+1,".")
    print("The previous number for the number",number,"is",number-1,".")
