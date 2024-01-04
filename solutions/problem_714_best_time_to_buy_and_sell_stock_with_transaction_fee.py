# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        result = 0
        min_price = prices[0]
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            elif price - fee > min_price:
                result += price - fee - min_price
                min_price = price - fee
        return result
