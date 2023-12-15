# https://leetcode.com/problems/decode-string/description/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_length = current_string = ''
        for c in s:
            if c.isdigit():
                current_length += c
            elif c == '[':
                stack.append(current_string)
                stack.append(int(current_length))
                current_length = current_string = ''
            elif c == ']':
                decoded_string = current_string * stack.pop()
                current_string = stack.pop() + decoded_string
            else:
                current_string += c
        return current_string
                
                
