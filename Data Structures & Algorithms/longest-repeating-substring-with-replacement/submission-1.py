class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        count = {}
        l = 0
        for r in range(len(s)):
            curr_len = r - l + 1
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1
            if curr_len - max(count.values()) <= k:
                result = max(result, r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1
        
        return result