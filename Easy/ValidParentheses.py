class Solution(object):
    def isValid(self, s):
        stack = []
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if char == ')':
                    if stack[-1] == '(':
                        stack.pop()
                elif char == '}':
                    if stack[-1] == '{':
                        stack.pop()
                elif char == ']':
                    if stack[-1] == '[':
                        stack.pop()
        return len(stack) == 0
            
        
        