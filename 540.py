from collections import Counter 
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = Counter(nums)
        l1= sorted(l.items(), key = lambda x: x[1])
        return l1[0][0]