def add_sum(arr,k):
    arr2 = arr
    for i in arr:
        n1 = k - i
        if(n1 in arr2):
            return True
    return False

print(add_sum([10,15,1,4],5))
