def lowest_Positive(arr):
    if(arr == []):
        return 1
    minm = max(arr)+1
    if 1 not in arr:
        return 1
    for i in range(len(arr)):
        if(arr[i]>=0):
            if(arr[i]+1 not in arr and minm > arr[i]+1):
                minm = arr[i] + 1
    return minm
print(lowest_Positive([]))