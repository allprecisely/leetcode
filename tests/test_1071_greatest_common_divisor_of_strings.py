import pytest

from solutions.problem_1071_greatest_common_divisor_of_strings import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (('ABCABC', 'ABC'), 'ABC'),
        (('ABABAB', 'ABAB'), 'AB'),
        (('LEET', 'CODE'), ''),
        # my checks
        (('A', 'A'), 'A'),
        (('AA', 'A'), 'A'),
        (('AA', 'AA'), 'AA'),
        (('AAA', 'AA'), 'A'),
        (('AAAB', 'AAA'), ''),
        (('AAABAAA', 'AAABAAAA'), ''),
        (('AAABAAA', 'AAABAAA'), 'AAABAAA'),
    ],
)
def test_solution(input, output):
    assert output == instance.gcdOfStrings(*input)
