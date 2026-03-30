class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        #get num of occurences in s1
        seen = [0] * 26
        for c in s1:
            seen[ord(c) - ord('a')] += 1

        #use sliding window of len(s1) to check for substrings across s2

        #decide sliding window size
        #init first window
        window = [0] * 26
        for i in range(len(s1)):
            window[ord(s2[i]) - ord('a')] += 1

        #check if the init window contains a permutation
        if seen == window:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            window[ord(s2[l]) - ord('a')] -= 1
            l += 1

            window[ord(s2[r]) - ord('a')] += 1
            if seen == window:
                return True

        return False





