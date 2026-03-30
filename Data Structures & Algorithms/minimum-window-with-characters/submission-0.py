class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        seen = {}
        for c in t:
            if c not in seen:
                seen[c] = 1
            else:
                seen[c] += 1

        l = 0
        have, need = 0, len(seen)
        res = 0
        window = {}
        res, resLen = [-1, -1], float("infinity")
        for r in range(len(s)):
            if s[r] not in window:
                window[s[r]] = 1
            else:
                window[s[r]] += 1
                
            if s[r] in seen and window[s[r]] == seen[s[r]]:
                have += 1

            while need == have:
                print(need)
                print(have)
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in seen and window[s[l]] < seen[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r + 1] if resLen != float('infinity') else ""

                
            


