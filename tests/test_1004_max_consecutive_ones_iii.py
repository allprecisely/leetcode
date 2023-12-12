import pytest

from solutions.problem_1004_max_consecutive_ones_iii import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (([1,1,1,0,0,0,1,1,1,1,0], 2), 6),
        (([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3), 10),
        # my checks
        (([0], 0), 0),
        (([0], 1), 1),
        (([1], 0), 1),
        (([1], 1), 1),
        (([0, 0], 0), 0),
        (([0, 0], 1), 1),
        (([0, 0], 3), 2),
        (([1, 0], 3), 2),
        (([1, 1], 3), 2),
    ],
)
def test_solution(input_data, output):
    assert output == instance.longestOnes(*input_data)
