class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #can i compare with ord(c) - ord('a') and see if thats greater than ord(c+1) - ord('a')
        #if right pointer reaches a a char that is seen already move left to 

        #if ord(r) - ord('a') < ord(l) - ord('a') then widnow should shrink

        l = 0
        result = 0
        char_set = set()
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1
            result = max(result, r - l + 1)
            char_set.add(s[r])
        return result