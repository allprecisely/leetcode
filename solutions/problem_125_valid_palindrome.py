# https://leetcode.com/problems/valid-palindrome/description/
# 2 tries

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_index, right_index = 0, len(s) - 1
        while left_index < right_index:
            while left_index < right_index and not s[left_index].isalnum():
                left_index += 1
            while right_index > left_index and not s[right_index].isalnum():
                right_index -= 1
            if s[left_index].upper() != s[right_index].upper():
                return False
            left_index += 1
            right_index -= 1
        return True