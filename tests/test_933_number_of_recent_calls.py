import pytest

from solutions.problem_933_number_of_recent_calls import RecentCounter


@pytest.mark.parametrize(
    'input, output',
    [
        ([[], [1], [100], [3001], [3002]], [None, 1, 2, 3, 3]),
        # my checks
        ([[], [1]], [None, 1]),
        ([[], [3000], [6001], [6002]], [None, 1, 1]),
    ],
)
def test_solution(input, output):
    instance = RecentCounter()
    for i, j in zip(input[1:], output[1:]):
        assert instance.ping(i[0]) == j
