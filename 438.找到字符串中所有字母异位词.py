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
        a=[0]*26#滑动窗口与p的字符比较情况
        ans=[]
        for i in range(n):
            a[ord(s[i])-ord('a')]+=1
            a[ord(p[i])-ord('a')]-=1

        differ=[c!=0 for c in a].count(True)#不一样的字符个数
        if differ==0:ans.append(0)
        for i in range(m-n):
            if a[ord(s[i])-ord('a')]==1:#如果这个字符本来p必滑动窗口多一个，现在减去了
                differ-=1
            elif a[ord(s[i])-ord('a')]==0:
                differ+=1
            a[ord(s[i])-ord('a')]-=1
            if a[ord(s[i+n])-ord('a')]==0:
                differ+=1
            elif a[ord(s[i+n])-ord('a')]==-1:
                differ-=1
            a[ord(s[i+n])-ord('a')]+=1

            if differ==0:ans.append(i+1)
        
        return ans

# @lc code=end

