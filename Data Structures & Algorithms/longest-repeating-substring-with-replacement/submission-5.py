class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        res = 0
        count = {}
        #slide r pointer and increase window size
        for r in range(len(s)):
            #increment the count of that char
            count[s[r]] = count.get(s[r], 0) + 1
            #if there are >k chars to remove shrink window
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            #update the res to be the max substring
            res = max(res, r - l + 1)

        return res
            
            
