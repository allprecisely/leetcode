import pytest

from solutions.problem_2352_equal_row_and_column_pairs import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(grid = [[3,2,1],[1,7,6],[2,7,7]]), 1),
        (dict(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]), 3),
        # my checks
        (dict(grid = [[1]]), 1),
        (dict(grid = [[1, 1], [1, 1]]), 4),
        (dict(grid = [[1, 2], [2, 1]]), 2),
        (dict(grid = [[1, 2], [3, 4]]), 0),
        (dict(grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]), 9),

    ],
)
def test_solution(input, output):
    assert output == instance.equalPairs(**input)
