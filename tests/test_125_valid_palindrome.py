import pytest

from solutions.problem_125_valid_palindrome import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ('A man, a plan, a canal: Panama', True),
        ('race a car', False),
        (' ', True),
        # my checks
        ('', True),
        ('a', True),
        ('aA', True),
        ('ab', False),
        ('aba', True),
        ('abab', False),
        # after fails
        ('.,', True)
    ],
)
def test_solution(input_data, output):
    assert instance.isPalindrome(input_data) == output
