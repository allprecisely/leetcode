import pytest

from solutions.problem_746_min_cost_climbing_stairs import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(cost = [10,15,20]), 15),
        (dict(cost = [1,100,1,1,1,100,1,1,100,1]), 6),
        # my checks
        (dict(cost = [1, 2]), 1),
        (dict(cost = [2, 1]), 1),
        (dict(cost = [2, 1, 1, 2]), 2),
        (dict(cost = [1, 2, 2, 1]), 3),
        # after wrong
        (dict(cost = [0, 2, 2, 1]), 2),
    ],
)
def test_solution(input_data, output):
    assert output == instance.minCostClimbingStairs(**input_data)
