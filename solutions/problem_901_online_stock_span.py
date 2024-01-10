# https://leetcode.com/problems/online-stock-span/description/

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        result = 1
        while self.stack and price > self.stack[-1][0]:
            result += self.stack.pop()[1]
        self.stack.append((price, result))
        return result
