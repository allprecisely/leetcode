import pytest

from solutions.problem_2462_total_cost_to_hire_k_workers import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4), 11),
        (dict(costs = [1,2,4,1], k = 3, candidates = 3), 4),
        # my checks
        (dict(costs = [1], k = 1, candidates = 1), 1),
        (dict(costs = [1, 2], k = 1, candidates = 2), 1),
        (dict(costs = [1, 2], k = 2, candidates = 1), 3),
        (dict(costs = [1, 2, 3], k = 1, candidates = 1), 1),
        (dict(costs = [1, 2, 3], k = 2, candidates = 1), 3),
        # after wrong
        (dict(costs = [31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], k = 11, candidates = 2), 423),
        # 25 31 72 74   58 17 33 9 27 59 18
    ],
)
def test_solution(input_data, output):
    assert output == instance.totalCost(**input_data)
