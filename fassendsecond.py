def ascending(s, e, arr):
    arr[s:e+1] = sorted(arr[s:e+1])  

def descending(s, e, arr):
    arr[s:e+1] = sorted(arr[s:e+1], reverse=True)  

arr = [1, 7, 5, 4, 8, 6]
mid = (len(arr) - 1) // 2  

ascending(0, mid, arr)
descending(mid + 1, len(arr) - 1, arr)

print(" ".join(map(str, arr)))  
