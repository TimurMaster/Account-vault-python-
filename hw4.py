n = int(input())
k = int(input())
c = k % n
if ((n < 1 or n > 9999) or (k < 1 or k > 9999) ):
    print("Превышен лимит!")
else:
    print(c)