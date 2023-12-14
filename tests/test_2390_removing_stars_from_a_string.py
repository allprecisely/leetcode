import pytest

from solutions.problem_2390_removing_stars_from_a_string import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(s = "leet**cod*e"), 'lecoe'),
        (dict(s = "erase*****"), ''),
        # my checks
        (dict(s = 'a'), 'a'),
        (dict(s = 'ab'), 'ab'),
        (dict(s = 'ab*'), 'a'),
        (dict(s = 'a*b'), 'b'),
        (dict(s = 'ab**'), ''),
        (dict(s = 'a*b*'), ''),

    ],
)
def test_solution(input, output):
    assert output == instance.removeStars(**input)
