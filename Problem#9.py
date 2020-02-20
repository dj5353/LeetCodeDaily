def largest_adj(nums):
        length = len(nums)
        if length==0:
            return 0
        if length==1:
            return nums[0]
        if length==2:
            return max(nums)
        dp = [0]*length
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, length):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return max(dp)
print(largest_adj([5,1,1,5]))