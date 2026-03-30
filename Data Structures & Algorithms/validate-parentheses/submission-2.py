class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {'}':'{', ']':'[', ')':'('}
        stack = []
        for c in s:
            if c in dictionary and stack and dictionary[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)


        return len(stack) == 0