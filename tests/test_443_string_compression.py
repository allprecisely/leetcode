import pytest

from solutions.problem_443_string_compression import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output, changed_input',
    [
        (['a','a','b','b','c','c','c'], 6, ["a","2","b","2","c","3"]),
        (['a'], 1, ['a']),
        (['a','b','b','b','b','b','b','b','b','b','b','b','b'], 4, ["a","b","1","2"]),
        # my checks
        (['a', 'b'], 2, ['a', 'b']),
        (['a', 'a'], 2, ['a', '2']),
        (['a', 'a', 'a'], 2, ['a', '3']),
        (['a', 'a', 'b'], 3, ['a', '2', 'b']),
        (['a', 'b', 'a', 'b', 'a'], 5, ['a', 'b', 'a', 'b', 'a']),
    ],
)
def test_solution(input_data, output, changed_input):
    assert output == instance.compress(input_data)
    assert input_data[:output] == changed_input
