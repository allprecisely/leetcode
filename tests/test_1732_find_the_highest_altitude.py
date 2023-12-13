import pytest

from solutions.problem_1732_find_the_highest_altitude import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(gain = [-5,1,5,0,-7]), 1),
        (dict(gain = [-4,-3,-2,-1,4,3,2]), 0),
        #dict(num =  my check)s
        (dict(gain = [-5]), 0),
        (dict(gain = [5]), 5),
        (dict(gain = [0, 0, 0, 0, 0]), 0),
        (dict(gain = [-5, 5]), 0),
        (dict(gain = [5, -5]), 5),
        (dict(gain = [-1, -1, -1]), 0),
    ],
)
def test_solution(input, output):
    assert output == instance.largestAltitude(**input)
