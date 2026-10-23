class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if char == ')':
                    if (len(stack) > 0) and ((stack[-1] == '(')):
                        stack.pop()
                    else:
                        return False
                elif char == '}':
                    if (len(stack) > 0) and ((stack[-1] == '{')):
                        stack.pop()
                    else:
                        return False
                elif char == ']':
                    if (len(stack) > 0) and ((stack[-1] == '[')):
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0