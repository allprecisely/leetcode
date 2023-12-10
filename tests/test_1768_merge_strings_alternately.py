import pytest

from solutions.problem_1768_merge_strings_alternately import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (('abc', 'pqr'), 'apbqcr'),
        (('ab', 'pqrs'), 'apbqrs'),
        (('abcd', 'pq'), 'apbqcd'),
        # my checks
        (('a', 'b'), 'ab'),
        (('a', 'bcd'), 'abcd'),
        (('acd', 'b'), 'abcd'),
    ],
)
def test_solution(input_data, output):
    assert output == instance.mergeAlternately(*input_data)
