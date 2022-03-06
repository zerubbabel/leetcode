#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#

# @lc code=start


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        #找到left,right它们对应的二进制字符串的公共前缀
        if left==right:return left
        def convert(x):
            s=[]
            while x:
                s.append(x%2)
                x//=2
            return s
        
        a=convert(left)
        b=convert(right)
        m,n=len(a),len(b)
        for i in range(n-m):
            a.append(0)
        k=n-1
        s=0
        for i in range(n-1,-1,-1):
            if a[i]!=b[i]:
                k=i
                break
            s=s*2+a[i]
        if k==n-1:return 0
        return s<<(k+1)
        
        
# @lc code=end

