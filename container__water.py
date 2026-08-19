class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        res=0 
        while l<r:
            length= min(height[l],height[r])
            breadth= r-l
            res= max(res, length*breadth)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res
