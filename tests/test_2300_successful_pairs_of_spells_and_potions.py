import pytest

from solutions.problem_2300_successful_pairs_of_spells_and_potions import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(spells = [5,1,3], potions = [1,2,3,4,5], success = 7), [4,0,3]),
        (dict(spells = [3,1,2], potions = [8,5,8], success = 16), [2,0,2]),
        # my checks
        (dict(spells = [1], potions = [2], success = 2), [1]),
        (dict(spells = [7], potions = [11], success = 78), [0]),

    ],
)
def test_solution(input_data, output):
    assert output == instance.successfulPairs(**input_data)
