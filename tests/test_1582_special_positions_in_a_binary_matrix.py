import pytest

from solutions.problem_1582_special_positions_in_a_binary_matrix import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(mat = [[1,0,0],[0,0,1],[1,0,0]]), 1),
        (dict(mat = [[1,0,0],[0,1,0],[0,0,1]]), 3),
        # my checks
        (dict(mat = [[1]]), 1),
        (dict(mat = [[0]]), 0),
        (dict(mat = [[0, 1]]), 1),
        (dict(mat = [[1, 0]]), 1),
        (dict(mat = [[1, 1]]), 0),
        (dict(mat = [[0, 0]]), 0),
        (dict(mat = [[0, 0], [0, 0]]), 0),
        (dict(mat = [[1, 0], [0, 0]]), 1),
        (dict(mat = [[1, 0], [1, 0]]), 0),
        (dict(mat = [[1, 1], [0, 0]]), 0),

    ],
)
def test_solution(input, output):
    assert output == instance.numSpecial(**input)
