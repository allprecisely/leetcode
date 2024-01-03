import pytest

from solutions.problem_790_domino_and_tromino_tiling import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(n = 3), 5),
        (dict(n = 1), 1),
        # my checks
        (dict(n = 2), 2),
        (dict(n = 4), 11),
    ],
)
def test_solution(input, output):
    assert output == instance.numTilings(**input)
