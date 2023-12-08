import pytest

from solutions.problem_1903_largest_odd_number_in_string import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        ("52", "5"),
        ("4206", ""),
        ("35427", "35427"),
        # my checks
        ("1", "1"),
        ("2", ""),
        ("258", "25"),
        ("123278958", "12327895"),
    ],
)
def test_solution(input, output):
    assert output == instance.largestOddNumber(input)
