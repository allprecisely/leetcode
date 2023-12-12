# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/

from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        result = 0
        pairs = {}
        for num in nums:
            if pairs.get(num, 0) != 0:
                pairs[num] -= 1
                result += 1
            elif k - num > 0:
                pairs[k - num] = pairs.get(k - num, 0) + 1
        return result