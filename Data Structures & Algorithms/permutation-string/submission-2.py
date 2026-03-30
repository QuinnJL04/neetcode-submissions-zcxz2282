class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        seen = [0] * 26
        window = [0] * 26
        for c in s1:
            seen[ord(c) - ord('a')] += 1

        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1

        if seen == window:
            return True

        l = 0
        for j in range(len(s1), len(s2)):
            window[ord(s2[l]) - ord('a')] -= 1
            l+=1

            window[ord(s2[j]) - ord('a')] += 1

            if seen == window:
                return True
        return False
      

       
            
        
        



        


        