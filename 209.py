class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target: 
            return 0
        if sum(nums)== target:
            return len(nums)
        if target in nums:
            return 1
        left = 0 
        ans = float('inf')
        sm=0 
        for right in range(len(nums)):
            sm= sm+nums[right]
            while sm>= target:
                ans = min(ans, right- left+1 )
                sm = sm- nums[left]
                left+=1
        return ans