import pytest

from solutions.problem_714_best_time_to_buy_and_sell_stock_with_transaction_fee import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(prices = [1,3,2,8,4,9], fee = 2), 8),
        (dict(prices = [1,3,7,5,10,3], fee = 3), 6),
        # my checks
        (dict(prices = [1, 4, 3, 7], fee = 2), 4),
        (dict(prices = [2], fee = 2), 0),
        (dict(prices = [2, 3], fee = 1), 0),
        (dict(prices = [2, 3], fee = 0), 1),
        (dict(prices = [2, 1], fee = 0), 0),
    ],
)
def test_solution(input, output):
    assert output == instance.maxProfit(**input)