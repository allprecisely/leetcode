# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > result:
                result = price - min_price
        return result
            