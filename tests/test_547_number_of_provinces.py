import pytest

from solutions.problem_547_number_of_provinces import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(isConnected = [[1,1,0],[1,1,0],[0,0,1]]), 2),
        (dict(isConnected = [[1,0,0],[0,1,0],[0,0,1]]), 3),
        # my checks
        (dict(isConnected = [[1]]), 1),
        (dict(isConnected = [[1, 1], [1, 1]]), 1),
        (dict(isConnected = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]), 1),
        (dict(isConnected = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]), 1),

    ],
)
def test_solution(input_data, output):
    assert output == instance.findCircleNum(**input_data)
    assert output == instance.findCircleNumRecursive(**input_data)
