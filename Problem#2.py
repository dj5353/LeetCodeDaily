# With Using Division operator

# def Product(arr):
#     prod = 1
#     arr2 = []
#     for i in arr:
#         prod *= i;
#     for i in arr:
#         arr2.append(prod/i)
#     return arr2

# print(Product([1,2,3,4,5]))


#Without using Division operator

def productExceptSelf(nums): 
        length = len(nums)
        answer = [0]*length
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]
        R = 1;
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer
print(productExceptSelf([1,2,3,4,5]))

