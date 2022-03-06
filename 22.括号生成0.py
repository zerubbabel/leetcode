#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def convert(x):
            a=[]
            for i in range(2*n):
                a.append(x%2)
                x=x//2
            return a
        def ok(t):
            v=0
            for x in t:
                if x==0:
                    v+=1
                else:
                    v-=1
                if v<0:return False
            return v==0
        def change(t):
            a=[]
            for x in t:
                if x==0:
                    a.append('(')
                else:
                    a.append(')')
            return ''.join(a)

        ans=[]
        for i in range(2**(2*n)):
            t=convert(i)
            if ok(t):
                ans.append(change(t))
        return ans

# @lc code=end

