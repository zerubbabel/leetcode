#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        n=len(digits)
        if n==0:return []
        a=[3]*5+[4,3,4]
        c=['a']
        for i in range(1,len(a)):
            c.append(chr(ord(c[-1])+a[i-1]))
        ans=[]
        def find(k,n,t):
            if k==n:
                ans.append(t)
                return
            j=ord(digits[k])-ord('2')
            for i in range(a[j]):
                find(k+1,n,t+chr(ord(c[j])+i))
        find(0,n,'')
        return ans
# @lc code=end

