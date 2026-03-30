class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        stack = []

        def dfs(need_open, need_close):
            if need_open == need_close == n:
                res.append("".join(stack))
                return
            
            if need_open < n:
                stack.append("(")
                dfs(need_open + 1, need_close)
                stack.pop()
            if need_close < need_open:
                stack.append(")")
                dfs(need_open, need_close + 1)
                stack.pop()
            
        dfs(0, 0)
        return res

            
            


        
        
        
        
        