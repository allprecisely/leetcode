import pytest

from solutions.problem_394_decode_string import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(s = "3[a]2[bc]"), 'aaabcbc'),
        (dict(s = "3[a2[c]]"), 'accaccacc'),
        (dict(s = "2[abc]3[cd]ef"), 'abcabccdcdcdef'),
        # my checks
        (dict(s = "a"), 'a'),
        (dict(s = "ab"), 'ab'),
        (dict(s = "1[a]"), 'a'),
        (dict(s = "1[a]1[a]"), 'aa'),
        (dict(s = "1[a]2[a]"), 'aaa'),
        (dict(s = "3[a]2[a]"), 'aaaaa'),
        (dict(s = "3[a]b2[a]"), 'aaabaa'),
        (dict(s = "b3[a]b2[a]b"), 'baaabaab'),
        (dict(s = "b3[a1[b]]b2[a]b"), 'babababbaab'),
        (dict(s = "2[a2[b2[c]d]e]f"), 'abccdbccdeabccdbccdef'),
    ],
)
def test_solution(input, output):
    assert output == instance.decodeString(**input)
