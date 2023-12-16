import pytest

from solutions.problem_1436_destination_city import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]), "Sao Paulo"),
        (dict(paths = [["B","C"],["D","B"],["C","A"]]), "A"),
        (dict(paths = [["A","Z"]]), "Z"),
        # my checks
    ],
)
def test_solution(input, output):
    assert output == instance.destCity(**input)
