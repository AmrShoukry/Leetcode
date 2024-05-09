class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        length = len(s)

        for i in range(length):
            if s[i] == '(' or s[i] == '{'  or s[i] == '[':
                stack.append(s[i])
            elif not stack or (s[i] == ')' and stack[-1] != '(') or (s[i] == '}' and stack[-1] != '{') or (s[i] == ']' and stack[-1] != '['):
                return False
            else:
                stack.pop()
        if not stack:
            return True
        return False

