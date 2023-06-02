n = int(input())
arr =list(map(int, input().strip().split()))

arr = sorted(arr)
for i in range(len(arr)-2, -1, -1):
    if(arr[i] < arr[-1]):
        print(arr[i])
        break