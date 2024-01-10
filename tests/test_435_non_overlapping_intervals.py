import pytest

from solutions.problem_435_non_overlapping_intervals import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(intervals = [[1,2],[2,3],[3,4],[1,3]]), 1),
        (dict(intervals = [[1,2],[1,2],[1,2]]), 2),
        (dict(intervals = [[1,2],[2,3]]), 0),
        # my checks
        (dict(intervals=[[1, 4], [4, 8], [3, 5]]), 1),
    ],
)
def test_solution(input_data, output):
    assert output == instance.eraseOverlapIntervals(**input_data)
