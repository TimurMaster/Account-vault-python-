arr = []
n = int(input())
i = 0
for i in range(n):
    if(n >= 1 and n <= 10 ** 5):
        value = int(input())
        if(value >= 0 and value <= 10 ** 9):
            arr.append(value)
        else:
            print("Error")
    else:
        print("Error")

def findSubsequence(arr):
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                print(arr[i])



findSubsequence(arr)