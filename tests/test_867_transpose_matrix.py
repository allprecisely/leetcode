import pytest

from solutions.problem_867_transpose_matrix import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ([[1,2,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]]),
        ([[1,2,3],[4,5,6]], [[1,4],[2,5],[3,6]]),
        # my checks
        ([[1]], [[1]]),
        ([[1, 2]], [[1], [2]]),
        ([[1], [2]], [[1, 2]]),

    ],
)
def test_solution(input_data, output):
    assert output == instance.transpose(input_data)
