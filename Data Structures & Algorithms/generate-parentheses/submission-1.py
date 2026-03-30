class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #use backtracking to explore all possibilities. 
        #u know a string is invalid when open parentheses exceeds closed parentheses
        #make backtracking algorithm and at each step decide to add a open or closed parentheses depending on if open > close or oppen < n
        #call backtrack to create a new branch until all conditions of a valid parentheses is matched and append it to the result.
        #after returning to a previous branch pop the end of stack off and explore other branches
        result = []
        stack = []

        def backtrack(opens,closes):
            if opens == closes == n:
                result.append("".join(stack))
                return

            if opens > closes:
                stack.append(")")
                backtrack(opens, closes + 1)
                stack.pop()

            if opens < n:
                stack.append("(")
                backtrack(opens +1, closes)
                stack.pop()

        backtrack(0, 0)

        return result