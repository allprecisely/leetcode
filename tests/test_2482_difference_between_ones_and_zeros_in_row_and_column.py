import pytest

from solutions.problem_2482_difference_between_ones_and_zeros_in_row_and_column import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(grid = [[0,1,1],[1,0,1],[0,0,1]]), [[0,0,4],[0,0,4],[-2,-2,2]]),
        (dict(grid = [[1,1,1],[1,1,1]]), [[5,5,5],[5,5,5]]),
        # my checks
        (dict(grid = [[1]]), [[2]]),
        (dict(grid = [[0]]), [[-2]]),
        (dict(grid = [[0, 0]]), [[-3, -3]]),
        (dict(grid = [[0, 1]]), [[-1, 1]]),
        (dict(grid = [[1, 0]]), [[1, -1]]),
        (dict(grid = [[1, 1]]), [[3, 3]]),
    ],
)
def test_solution(input_data, output):
    assert output == instance.onesMinusZeros(**input_data)
