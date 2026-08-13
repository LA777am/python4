class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        l=[]
        s=set()
        nums=sorted(nums)
        for i1, i in enumerate(nums):
            left =i1+1
            right = len(nums)-1
            while left<right:
                if i+nums[left]+nums[right]==0:
                    s.add((i ,nums[left],nums[right]))
                    left+=1
                    right-=1
                    continue
                elif nums[left]+nums[right]<-i:
                    left+=1
                    continue
                else:
                    right-=1
        return [list(k) for k in s]
                    
                



