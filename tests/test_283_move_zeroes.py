import pytest

from solutions.problem_283_move_zeroes import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ([0,1,0,3,12], [1,3,12,0,0]),
        ([0], [0]),
        # my checks
        ([1], [1]),
        ([0, 1], [1, 0]),
        ([0, 0], [0, 0]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 0, 2], [1, 2, 0]),
        ([0, 1, 2], [1, 2, 0]),
        ([1, 2, 0], [1, 2, 0]),
        ([1, 2, 3], [1, 2, 3]),
    ],
)
def test_solution(input_data, output):
    instance.moveZeroes(input_data)
    assert output == input_data
