import pytest

from solutions.problem_392_is_subsequence import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (('abc', 'ahbgdc'), True),
        (('axc', 'ahbgdc'), False),
        # my checks
        (('a', 'a'), True),
        (('', 'a'), True),
        (('', ''), True),
        (('a', ''), False),
        (('a', 'b'), False),
        (('a', 'ab'), True),
        (('a', 'ba'), True),
        (('abcd', 'abcb'), False),
    ],
)
def test_solution(input_data, output):
    assert output == instance.isSubsequence(*input_data)
