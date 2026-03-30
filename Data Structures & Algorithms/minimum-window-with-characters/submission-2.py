class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        seen = {}
        for c in t:
            seen[c] = seen.get(c, 0) + 1
        
        have, need = 0, len(seen)
        res, resLen = [-1, -1], float('inf')
        l=0
        window = {}
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in seen and window[c] == seen[c]:
                have += 1

            while need == have:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in seen and window[s[l]] < seen[s[l]]:
                    have -= 1 
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""
            
            


        

                
            


