import pytest

from solutions.problem_994_rotting_oranges import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(grid = [[2,1,1],[1,1,0],[0,1,1]]), 4),
        (dict(grid = [[2,1,1],[0,1,1],[1,0,1]]), -1),
        (dict(grid = [[0,2]]), 0),
        # my checks
        (dict(grid = [[0]]), 0),
        (dict(grid = [[1]]), -1),
        (dict(grid = [[2]]), 0),
        (dict(grid = [[2, 0]]), 0),
        (dict(grid = [[2, 1]]), 1),
        (dict(grid = [[1, 2]]), 1),
        (dict(grid = [[2, 2]]), 0),
        (dict(grid = [[1, 1]]), -1),
        (dict(grid = [[1, 0]]), -1),
        (dict(grid = [[0, 1]]), -1),
        (dict(grid = [[1], [2]]), 1),
        (dict(grid = [[2], [1]]), 1),
    ],
)
def test_solution(input_data, output):
    assert output == instance.orangesRotting(**input_data)

test_solution(dict(grid = [[2, 2]]), 0),