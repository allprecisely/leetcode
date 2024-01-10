import pytest

from solutions.problem_452_minimum_number_of_arrows_to_burst_balloons import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(points = [[10,16],[2,8],[1,6],[7,12]]), 2),
        (dict(points = [[1,2],[3,4],[5,6],[7,8]]), 4),
        (dict(points = [[1,2],[2,3],[3,4],[4,5]]), 2),
        # my checks
        (dict(points=[[-2, -1], [-1, 2], [-4, -1], [-1, 0]]), 1),
    ],
)
def test_solution(input_data, output):
    assert output == instance.findMinArrowShots(**input_data)
