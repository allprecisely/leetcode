import pytest

from solutions.problem_649_dota2_senate import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(senate = "RD"), "Radiant"),
        (dict(senate = "RDD"), "Dire"),
        # my checks
        (dict(senate = "DDRRR"), "Dire"),
        (dict(senate = "DRDRR"), "Dire"),
        (dict(senate = "DRRDR"), "Radiant"),
        (dict(senate = "DDRRRR"), "Radiant"),
        (dict(senate = "DDDRRRRR"), "Radiant"),
        (dict(senate = "DDDDRRRRRR"), "Dire"),
    ],
)
def test_solution(input, output):
    assert output == instance.predictPartyVictory(**input)
