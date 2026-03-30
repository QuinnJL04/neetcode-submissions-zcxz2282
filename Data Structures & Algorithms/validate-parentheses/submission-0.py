class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lib = {"}":"{", ")":"(", "]":"["}

        for i in range(len(s)):
            if s[i] not in lib:
                stack.append(s[i])
            elif stack and stack[-1] == lib[s[i]]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0