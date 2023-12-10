import pytest

from solutions.problem_242_valid_anagram import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (('anagram', 'nagaram'), True),
        (('rat', 'cat'), False),
        # my checks
        (('', ''), True),
        (('a', 'a'), True),
        (('a', ''), False),
        (('', 'a'), False),
        (('b', 'a'), False),
        (('ab', 'aa'), False),
        (('aba', 'aab'), True),
        (('ccc', 'ccc'), True),
        (('cccc', 'ccc'), False),

    ],
)
def test_solution(input_data, output):
    assert instance.isAnagram(*input_data) == output
