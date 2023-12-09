# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'}': '{', ')': '(', ']': '['}
        stack = []
        for c in s:
            if c in pairs:
                if not (stack and stack.pop() == pairs[c]):
                    return False
            else:
                stack.append(c)
        return not stack

