st = str(input())
ln = len(st)
if ln > 100:
    print("Длина символов превышает лимит: ")
else:
    print("Hello, ", "!", sep = st)