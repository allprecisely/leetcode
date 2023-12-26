import pytest

from solutions.problem_198_house_robber import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(nums = [1,2,3,1]), 4),
        (dict(nums = [2,7,9,3,1]), 12),
        # my checks
        (dict(nums = [2, 1, 1, 2]), 4),
        (dict(nums = [1, 2, 2, 1]), 3),
        (dict(nums = [1]), 1),
        (dict(nums = [1, 3]), 3),
        (dict(nums = [1, 3, 1]), 3),
        (dict(nums = [1, 1, 3]), 4),
        (dict(nums = [1, 1, 1]), 2),
    ],
)
def test_solution(input_data, output):
    assert output == instance.rob(**input_data)
