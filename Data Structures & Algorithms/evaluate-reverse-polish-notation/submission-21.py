class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        stack = []
        i = 0

        #loop through tokens if its a num add it to stack

        #else we pop twice and do operand and append to a res

        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            elif i == '+':
                summ = int(stack.pop()) + int(stack.pop())
                stack.append(summ)
            elif i == '*':
                prod = int(stack.pop()) * int(stack.pop())
                stack.append(prod)
            elif i == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                quot = b /a 
                stack.append(int(quot))
            else:
                a, b = stack.pop(), stack.pop()
                diff = int(b) - int(a)
                stack.append(diff)
        return stack[-1]
                