class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = list()
        operands = ('+', '-', '/', '*')

        for i in range(len(tokens)):

            if tokens[i] in operands:

                token = tokens[i]

                right = int(stack.pop())
                left = int(stack.pop())

                if token =='+':
                    ans = left + right
                    stack.append(ans)
                elif token =='-':
                    ans = left - right
                    stack.append(ans)
                elif token =='/':
                    ans = left / right
                    stack.append(ans)
                elif token =='*':
                    ans = left*right
                    stack.append(ans)

            else:
                stack.append(tokens[i])

        return int(stack[-1])







        