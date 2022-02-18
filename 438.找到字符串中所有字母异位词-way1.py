#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m,n=len(s),len(p)
        if m<n:return []
        a,b=[0]*26,[0]*26
        ans=[]
        for i in range(n):
            a[ord(s[i])-ord('a')]+=1
            b[ord(p[i])-ord('a')]+=1
        if a==b:ans.append(0)
        for i in range(m-n):
            a[ord(s[i])-ord('a')]-=1
            a[ord(s[i+n])-ord('a')]+=1
            if a==b:ans.append(i+1)
        
        return ans

# @lc code=end

