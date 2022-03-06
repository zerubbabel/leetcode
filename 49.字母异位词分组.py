#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h=[]
        for x in strs:
            t={}
            for c in x:
                if c in t:
                    t[c]+=1
                else:
                    t[c]=1
            h.append(t)
        n=len(strs)
        b=[0]*n
        ans=[]
        for i in range(n):
            if b[i]==0:
                t=[strs[i]]
                for j in range(i+1,n):
                    if b[j]==0 and h[i]==h[j]:
                        t.append(strs[j])
                        b[j]=1
                ans.append(t)
        return ans



# @lc code=end

