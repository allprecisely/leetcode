import pytest

from solutions.problem_20_valid_parentheses import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ('()', True),
        ('()[]{}', True),
        ('(]', False),
        # my checks
        ('(', False),
        (')', False),
        (')(', False),
        ('(())', True),
        ('()()', True),
        ('(()())', True),
        ('([)]', False),
    ],
)
def test_solution(input_data, output):
    assert instance.isValid(input_data) == output
