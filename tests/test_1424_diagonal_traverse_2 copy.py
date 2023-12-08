import pytest

from solutions.problem_1424_diagonal_traverse_2 import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        ([[1,2,3],[4,5,6],[7,8,9]], [1,4,2,7,5,3,8,6,9]),
        ([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]], [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]),
        # my checks
        ([[0]], [0]),
        ([list(range(100))], list(range(100))),
        ([[i] for i in range(100)], list(range(100))),
        ([[0, 1, 2, 3], [1, 2]], [0, 1, 1, 2, 2, 3]),
        ([[1, 2], [0, 1, 2, 3]], [1, 0, 2, 1, 2, 3]),
        ([[0], [1], [2, 3]], [0, 1, 2, 3]),
    ],
)
def test_solution(input, output):
    assert output == instance.findDiagonalOrder(input)
