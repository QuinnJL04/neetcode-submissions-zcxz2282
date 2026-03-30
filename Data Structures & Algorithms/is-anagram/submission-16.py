class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        for c in s:
            if c not in seen:
                seen[c] = 1
            else:
                seen[c] += 1
        
        for c in t:
            if c in seen:
                seen[c] -= 1
            else:
                return False
        
        for key in seen.keys():
            if seen[key] > 0:
                return False
        
        return True