n = int(input())
n1 = '    _~_    '
n2 = '   (o o)   '
n3 = '  /  V  \  '
n4 = ' /(  _  )\ '
n5 = '   ^^ ^^   '
if n > 9 or n <= 0:
    print("Введите число от 1 до 9!")
    exit()
else:
    print(n1*n)
    print(n2*n)
    print(n3*n)
    print(n4*n)
    print(n5*n)