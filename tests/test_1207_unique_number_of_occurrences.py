import pytest

from solutions.problem_1207_unique_number_of_occurrences import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(arr = [1,2,2,1,1,3]), True),
        (dict(arr = [1,2]), False),
        (dict(arr = [-3,0,1,-3,1,1,1,-3,10,0]), True),
        # my checks
        (dict(arr = [1]), True),
        (dict(arr = [1, 1]), True),
        (dict(arr = [1, 1, 3]), True),
        (dict(arr = [1, 1, 3, 3]), False),
    ],
)
def test_solution(input, output):
    assert output == instance.uniqueOccurrences(**input)
