class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        #get occurences
        seen = [0] * 26
        for c in s1:
            seen[ord(c) - ord('a')] += 1
        
        #init window
        window = [0] * 26
        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1
        
        if window == seen:
                return True

        #slide the window
        l = 0
        for r in range(len(s1), len(s2)):
            window[ord(s2[l]) - ord('a')] -= 1
            l+=1
            window[ord(s2[r]) - ord('a')] += 1
            if window == seen:
                return True
        return False
            
            





