import pytest

from solutions.problem_1_two_sum import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (([2, 7, 11, 15], 9), [0, 1]),
        (([3, 2, 4], 6), [1, 2]),
        (([3, 3], 6), [0, 1]),
        (([-10, -50, 20], -30), [1, 2]),
    ],
)
def test_solution(input, output):
    assert set(instance.twoSum(*input)) == set(output)
