class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        res = []
        stack = []
        mapper = {
            2: ('a', 'b', 'c'),
            3: ('d', 'e', 'f'),
            4: ('g', 'h', 'i'),
            5: ('j', 'k', 'l'),
            6: ('m', 'n', 'o'),
            7: ('p', 'q', 'r', 's'),
            8: ('t', 'u', 'v'),
            9: ('w', 'x', 'y', 'z')
            }

        def dfs(i):

            if i >= len(digits):
                substr = "".join(stack.copy())
                res.append(substr)
                return
            
            num = int(digits[i])
            curr_tuple = mapper[num]

            for char in curr_tuple:
                stack.append(char)
                dfs(i + 1)
                stack.pop()
        
        dfs(0)
        return res
