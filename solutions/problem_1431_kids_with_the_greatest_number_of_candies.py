# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return [x + extraCandies >= max_candies for x in candies]




