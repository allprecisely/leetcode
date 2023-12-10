import pytest

from solutions.problem_151_reverse_words_in_a_string import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        ('the sky is blue', 'blue is sky the'),
        ('  hello world  ', 'world hello'),
        ('a good   example', 'example good a'),
        # my checks
        ('a', 'a'),
        ('abcd', 'abcd'),
        (' a  b   c    d     ', 'd c b a'),
    ],
)
def test_solution(input_data, output):
    assert output == instance.reverseWords(input_data)
