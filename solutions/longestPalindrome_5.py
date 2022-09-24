# 5. Longest Palindromic Substring


class Solution:
    def longestPalindrome(self, s: str) -> str:
        current_palindrome_start_index = 0
        current_palindrome_length = 1
        longest_palindrome_start_index = 0
        longest_palindrome_length = 1
        for i, c in enumerate(s[1:], 1):
            if current_palindrome_start_index - 1 < 0:
                current_palindrome_start_index = i - 1
                current_palindrome_length = 1
            if (
                current_palindrome_start_index - 1 >= 0
                and s[current_palindrome_start_index - 1] == c
            ):
                current_palindrome_start_index -= 1
                current_palindrome_length += 2
            elif s[i - 1] == c:
                current_palindrome_start_index = i - 1
                current_palindrome_length = 2
            else:
                current_palindrome_start_index = i
                current_palindrome_length = 1

            if longest_palindrome_length < current_palindrome_length:
                longest_palindrome_length = current_palindrome_length
                longest_palindrome_start_index = current_palindrome_start_index
        return s[
            longest_palindrome_start_index : longest_palindrome_start_index
            + longest_palindrome_length
        ]
