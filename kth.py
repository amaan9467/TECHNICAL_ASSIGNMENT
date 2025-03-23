import heapq

def kth_max_min(arr, k):
    min_heap = []  
    max_heap = []  

    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap) 

        heapq.heappush(max_heap, -num)  
        if len(max_heap) > k:
            heapq.heappop(max_heap)  

    return -max_heap[0], min_heap[0] 

arr = [1, 2, 3, 4, 5, 6]
k = int(input("Enter the value of K: "))

kth_min, kth_max = kth_max_min(arr, k)
print(f"The {k}th maximum element is {kth_max}")
print(f"The {k}th minimum element is {kth_min}")
