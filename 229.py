from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a= Counter(nums)
        n= []
        h= math.floor(len(nums)/3)
        for i,j in a.items():
            if j>h:
                n.append(i)
        return n 