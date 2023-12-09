import pytest

from solutions.problem_121_best_time_to_buy_and_sell_stock import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        # my checks
        ([1], 0),
        ([1, 2], 1),
        ([2, 1], 0),
        ([4, 7, 1, 5], 4),
        ([5, 6, 1, 2], 1),
    ],
)
def test_solution(input_data, output):
    assert instance.maxProfit(input_data) == output
