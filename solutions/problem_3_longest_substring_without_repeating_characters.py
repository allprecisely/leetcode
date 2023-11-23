# Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        char_places = {}
        start_pos = 0
        current_length = 0
        for i, c in enumerate(s):
            n = char_places.get(c)
            if n is None or n < start_pos:
                current_length += 1
            else:
                result = max(result, current_length)
                current_length = i - n
                start_pos = n + 1
            char_places[c] = i
        return max(result, current_length)
