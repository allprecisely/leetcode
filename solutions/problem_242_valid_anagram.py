# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_num = {}
        for c in s:
            char_num[c] = char_num.get(c, 0) + 1
        for c in t:
            if c not in char_num:
                return False
            char_num[c] -= 1
            if char_num[c] < 0:
                return False
        return all(v == 0 for v in char_num.values())
