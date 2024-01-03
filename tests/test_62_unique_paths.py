import pytest

from solutions.problem_62_unique_paths import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(m = 3, n = 7), 28),
        (dict(m = 3, n = 2), 3),
        # my checks
        (dict(m = 1, n = 1), 1),
        (dict(m = 4, n = 1), 1),
        (dict(m = 1, n = 4), 1),
        (dict(m = 2, n = 2), 2),
    ],
)
def test_solution(input, output):
    assert output == instance.uniquePaths(**input)
