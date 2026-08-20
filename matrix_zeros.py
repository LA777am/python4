class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        a= set()
        b= set()
        rows = len(matrix)
        cols= len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    a.add(i)
                    b.add(j)
        for i in a:
            for j in range(cols):
                matrix[i][j]=0
        for i in range(rows):
            for j in b:
                matrix[i][j]=0