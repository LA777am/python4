class Solution:
    def exist(self, board, word: str) -> bool:
        rows, cols= len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j]==word[0]:
                    print(board[i][j] , word[0])
                    curR=i 
                    curC=j
                    flag=True
                    for k in word[1::]:
                        if curR+1 < rows:
                            if board[curR+1][curC]==k:
                                curR+=1
                                print(board[curR][curC], k)
                        if curR-1> 0:
                            if board[curR-1][curC]==k:
                                curR-=1
                                print(board[curR][curC] , k)
                        if curC-1> 0:
                            if board[curR][curC-1]==k:
                                curC-=1
                                print(board[curR][curC] , k)
                        if curC+1< cols:
                            if board[curR][curC+1]==k:
                                curC+=1
                                print(board[curR][curC] , k)
                        if flag==False:
                            print(board[curR][curC] , k)
                            break

                    if flag and board[curR][curC]==word[-1]:
                        return True
        return False
                        
obj = Solution()
res= obj.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")
print(res)