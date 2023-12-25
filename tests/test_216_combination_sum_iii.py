import pytest

from solutions.problem_216_combination_sum_iii import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(k = 3, n = 7), [[1,2,4]]),
        (dict(k = 3, n = 9), [[1,2,6],[1,3,5],[2,3,4]]),
        (dict(k = 4, n = 1), []),
        # my checks
        (dict(k = 2, n = 10), [[1,9],[2,8],[3,7],[4,6]]),
        (dict(k = 2, n = 18), []),
        (dict(k = 3, n = 24), [[7,8,9]]),
        (dict(k = 9, n = 45), [[1,2,3,4,5,6,7,8,9]]),
        (dict(k = 9, n = 46), []),
        (dict(k = 9, n = 60), []),
        (dict(k = 9, n = 44), []),
        (dict(k = 8, n = 44), [[2,3,4,5,6,7,8,9]]),
    ],
)
def test_solution(input_data, output):
    assert set([frozenset(comb) for comb in output]) == set([frozenset(comb) for comb in instance.combinationSum3(**input_data)])
