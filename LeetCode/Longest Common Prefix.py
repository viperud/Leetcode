class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        n = len(strs)
        shorts = min(len(strs[0]), len(strs[n-1]))

        i = 0
        while(i < shorts and strs[0][i] == strs[n-1][i]):
            i += 1
    
        return strs[0][:i]