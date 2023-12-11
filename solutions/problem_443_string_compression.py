# https://leetcode.com/problems/string-compression/description/

from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        result = 0
        group_char = chars[0]
        group_length = 1
        for c in chars[1:]:
            if c == group_char:
                group_length += 1
            else:
                result += self.handle_group(chars, group_char, group_length, result)
                group_char = c
                group_length = 1
        result += self.handle_group(chars, group_char, group_length, result)
        return result

    def handle_group(
        self, chars: List[str], group_char: str, group_length: int, last_index: int
    ) -> int:
        group_compressed_length = 1
        chars[last_index] = group_char
        if group_length > 1:
            group_length_str = str(group_length)
            for i, digit in enumerate(group_length_str, last_index + 1):
                chars[i] = digit
            group_compressed_length += len(group_length_str)
        return group_compressed_length