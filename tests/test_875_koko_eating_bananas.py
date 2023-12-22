import pytest

from solutions.problem_875_koko_eating_bananas import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(piles = [3,6,7,11], h = 8), 4),
        (dict(piles = [30,11,23,4,20], h = 5), 30),
        (dict(piles = [30,11,23,4,20], h = 6), 23),
        # my checks
        (dict(piles = [10], h = 1), 10),
        (dict(piles = [10], h = 2), 5),
        (dict(piles = [10], h = 3), 4),
        (dict(piles = [10], h = 4), 3),
        (dict(piles = [10], h = 5), 2),
        (dict(piles = [10], h = 9), 2),
        (dict(piles = [10], h = 10), 1),
        (dict(piles = [10, 20], h = 2), 20),
        (dict(piles = [10, 20], h = 3), 10),
        (dict(piles = [10, 20], h = 4), 10),
        (dict(piles = [10, 20], h = 5), 7),
    ],
)
def test_solution(input_data, output):
    assert output == instance.minEatingSpeed(**input_data)
