import pytest

from solutions.problem_1903_largest_odd_number_in_string import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(num = "52"), "5"),
        (dict(num = "4206"), ""),
        (dict(num = "35427"), "35427"),
        # my checks
        (dict(num = "1"), "1"),
        (dict(num = "2"), ""),
        (dict(num = "258"), "25"),
        (dict(num = "123278958"), "12327895"),
    ],
)
def test_solution(input, output):
    assert output == instance.largestOddNumber(**input)
