import pytest

from solutions.problem_841_keys_and_rooms import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(rooms = [[1],[2],[3],[]]), True),
        (dict(rooms = [[1,3],[3,0,1],[2],[0]]), False),
        # my checks
        (dict(rooms = [[], [0, 1]]), False),
        (dict(rooms = [[0], [0, 1]]), False),
        (dict(rooms = [[1], []]), True),
        (dict(rooms = [[4], [2], [3], [], [1]]), True),
        (dict(rooms = [[4], [2], [3], [4], [1], []]), False),

    ],
)
def test_solution(input_data, output):
    assert output == instance.canVisitAllRooms(**input_data)
