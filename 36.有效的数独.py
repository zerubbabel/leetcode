#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def repetition(a):
            b=[0]*9
            for c in a:
                if '1'<=c<='9':
                    if b[ord(c)-ord('1')]>0:
                        return True
                    b[ord(c)-ord('1')]+=1
            return False
        
        for i in range(9):
            if repetition(board[i]):return False#row
            t,s=[],[]
            for j in range(9):
                t.append(board[j][i])
                s.append(board[i//3*3+j//3][i%3*3+j%3])
            if repetition(t):return False#column
            if repetition(s):return False#sub-box
        return True
# @lc code=end

