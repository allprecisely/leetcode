# https://leetcode.com/problems/is-subsequence/description/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len = len(s)

        if s_len > len(t):
            return False
        elif s_len == 0:
            return True

        s_index = 0
        for c in t:
            if s[s_index] == c:
                s_index += 1
                if s_index == s_len:
                    return True
        return False
