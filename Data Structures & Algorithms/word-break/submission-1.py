class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        #base pos case : if res == s : return True
        #default : return False

        dp = {len(s) : True}

        def dfs(i):

            if i in dp:
                return dp[i]
            
            for word in wordDict:
                idx = i + len(word)
                if idx <= len(s) and word == s[i:idx]:
                    if dfs(idx):
                        dp[idx] = True 
                        return True
            dp[idx] = False
            return False

        return dfs(0)
        
        

