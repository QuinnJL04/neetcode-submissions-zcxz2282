class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        res = 0
        i = 0
        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            seen.add(s[j])
            res = max(res, j - i + 1)
        return res




