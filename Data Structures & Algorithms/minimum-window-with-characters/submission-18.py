class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""
        
        #count occurences
        seen = {}
        for c in t:
            seen[c] = seen.get(c, 0) + 1
        have, need = 0, len(seen)

        window = {}
        res, res_len = [-1, -1], float('inf')
        l = 0
        for r in range(0, len(s)):
            window[s[r]] = window.get(s[r], 0) + 1

            if s[r] in seen and seen[s[r]] == window[s[r]]:
                have += 1

            while have == need:
                #update res
                window_len = r - l + 1
                if window_len < res_len:
                    res_len = window_len
                    res = [l, r]
                #update window
                window[s[l]] -= 1
                if s[l] in seen and window[s[l]] < seen[s[l]]:
                   have -= 1 
                l += 1

        l, r = res

        return s[l:r+1] if res_len < float('inf') else ""
            
            


                




            
            


        

                
            


