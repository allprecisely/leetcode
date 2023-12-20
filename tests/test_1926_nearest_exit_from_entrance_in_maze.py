import pytest

from solutions.problem_1926_nearest_exit_from_entrance_in_maze import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]), 1),
        (dict(maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]), 2),
        (dict(maze = [[".","+"]], entrance = [0,0]), -1),
        # my checks
        (dict(maze = [["."]], entrance = [0,0]), -1),
        (dict(maze = [[".", "."]], entrance = [0,0]), 1),
        (dict(maze = [[".", "."]], entrance = [0,1]), 1),
        (dict(maze = [["+", "."]], entrance = [0,1]), -1),
        (dict(maze = [[".", "+"]], entrance = [0,0]), -1),
        (dict(maze = [["."], ["+"]], entrance = [0,0]), -1),
        (dict(maze = [["+"], ["."]], entrance = [1,0]), -1),
        (dict(maze = [["."], ["."]], entrance = [1,0]), 1),
        (dict(maze = [["."], ["."]], entrance = [0,0]), 1),
        (dict(maze = [["+","+","+","+"],[".",".",".","."],["+","+","+","+"]], entrance = [1,0]), 3),
    ],
)
def test_solution(input_data, output):
    assert output == instance.nearestExit(**input_data)
