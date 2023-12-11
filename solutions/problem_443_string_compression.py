# https://leetcode.com/problems/string-compression/description/
# 1 try; improved a little, but it's mostly the same

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        chars_len = len(chars)

        if chars_len == 1:
            return 1
        
        result_length = group_start = 0
        
        for i, c in enumerate(chars):
            if chars_len == i + 1 or c != chars[i + 1]:
                chars[result_length] = c
                result_length += 1

                if i > group_start:
                    group_lenght = i - group_start + 1
                    for digit in str(group_lenght):
                        chars[result_length] = digit
                        result_length += 1
                group_start = i + 1
        return result_length