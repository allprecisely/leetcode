# https://leetcode.com/problems/edit-distance/description/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1: 
            return len(word2)
        dp = list(range(len(word1) + 1))
        for cur, c2 in enumerate(word2):
            dp[0] = cur
            for j, c1 in enumerate(word1):
                cur, dp[j + 1] = dp[j + 1], cur if c1 == c2 else min(dp[j + 1], cur, dp[j]) + 1
        return dp[-1]
