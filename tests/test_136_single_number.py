import pytest

from solutions.problem_136_single_number import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(nums = [2,2,1]), 1),
        (dict(nums = [4,1,2,1,2]), 4),
        (dict(nums = [1]), 1),
        # my checks
    ],
)
def test_solution(input_data, output):
    assert output == instance.singleNumber(**input_data)
