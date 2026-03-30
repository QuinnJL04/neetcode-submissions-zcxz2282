class Solution:
    def longestPalindrome(self, s: str) -> str:
        #if s[i] == s[j]
        #if inner is palindrome
        n = len(s)
        memo = [[False] * n for _ in range(n)]
        maxLen = 0

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length <= 2:
                        memo[i][j] = True
                    else:
                        #if outer chars are matching the current string is true if inner is true or its false if inner is false
                        memo[i][j] = memo[i + 1][j - 1]
            #update the new max string
                if memo[i][j] and length > maxLen:
                    start = i
                    maxLen = length
        
        return s[start:start + maxLen]
