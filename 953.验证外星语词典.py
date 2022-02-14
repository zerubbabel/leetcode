#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={}
        for i in range(len(order)):
            d[order[i]]=i

        n=len(words)
        # s>t return True
        def compare(s,t):
            m,n=len(s),len(t)
            for i in range(min(m,n)):
                if d[s[i]]>d[t[i]]:return True
                elif d[s[i]]<d[t[i]]:return False
            else:
                return m>n
            
        for i in range(1,n):
            if compare(words[i-1],words[i]):return False
        return True

# @lc code=end

