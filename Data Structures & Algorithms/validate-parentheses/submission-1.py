class Solution:
    def isValid(self, s: str) -> bool:

        stack = list()

        for bracket in s:
            if bracket in ['(','{','[']:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                if (stack[len(stack)-1] == '{' and bracket =='}') or (stack[len(stack)-1] == '[' and bracket ==']') or (stack[len(stack)-1] == '(' and bracket ==')'):
                    stack.pop()
                else:
                    return False
        if len(stack)!=0:
            return False
        return True


        