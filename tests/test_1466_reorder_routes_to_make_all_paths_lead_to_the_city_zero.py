import pytest

from solutions.problem_1466_reorder_routes_to_make_all_paths_lead_to_the_city_zero import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]), 3),
        (dict(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]), 2),
        (dict(n = 3, connections = [[1,0],[2,0]]), 0),
        # my checks
        (dict(n = 3, connections = [[0, 1]]), 1),
        (dict(n = 3, connections = [[1, 0]]), 0),
        (dict(n = 3, connections = [[1, 0], [2, 0]]), 0),
        (dict(n = 3, connections = [[1, 0], [2, 1]]), 0),
        (dict(n = 3, connections = [[1, 0], [2, 1], [3, 1]]), 0),
        (dict(n = 3, connections = [[1, 0], [2, 1], [3, 2]]), 0),
        (dict(n = 3, connections = [[1, 0], [2, 1], [3, 0]]), 0),
        (dict(n = 3, connections = [[0, 1], [0, 2], [0, 3]]), 3),
    ],
)
def test_solution(input_data, output):
    assert output == instance.minReorder(**input_data)
