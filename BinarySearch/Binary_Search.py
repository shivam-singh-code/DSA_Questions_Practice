
def iterative_binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while(low <= high):
        mid = int((low + high) / 2)
        if target == arr[mid]: return mid
        elif target > arr[mid]: low = mid + 1
        else: high = mid - 1

    return -1

def recursive_binary_search(arr, target, low, high):
    if low > high:
        return -1
    
    mid = int((low + high)/2)

    if target == arr[mid]:
        return mid
    elif target > arr[mid]:
        low = mid+1
        return recursive_binary_search(arr, target, low, high)
    else:
        high = mid - 1
        return recursive_binary_search(arr, target, low, high)
    
def binary_search(arr, target):
    return recursive_binary_search(arr, target, low=0, high=len(arr)-1)

arr = [3, 4, 6, 7, 9, 12, 16, 17]
target = 6

print(binary_search(arr, target))


# print(iterative_binary_search(arr, target))