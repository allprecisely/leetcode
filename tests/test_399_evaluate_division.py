import pytest

from solutions.problem_399_evaluate_division import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (
            dict(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]),
            [6.00000,0.50000,-1.00000,1.00000,-1.00000],
        ),
        (
            dict(equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]),
            [3.75000,0.40000,5.00000,0.20000],
        ),
        (
            dict(equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]),
            [0.50000,2.00000,-1.00000,-1.00000],
        ),
        # my checks
    ],
)
def test_solution(input_data, output):
    assert output == instance.calcEquation(**input_data)
