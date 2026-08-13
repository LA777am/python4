class Solution:
    def getRow(self, rowIndex: int):
        prevRow= []
        cur=[1]
        for i in range(0, rowIndex+1):
            cur= [1]*(i+1)
            flag = True
            if i > 0:
                for j in range(1, len(cur)-1):
                    if len(prevRow)>1:
                        cur[j]= prevRow[j]+prevRow[j-1]
                        flag =False
            prevRow= cur
            if i==rowIndex:
                return prevRow
s = Solution()
ans = s.getRow(rowIndex=1111111110)
print(ans)