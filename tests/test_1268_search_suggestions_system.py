import pytest

from solutions.problem_1268_search_suggestions_system import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (
                dict(products=["mobile", "mouse", "moneypot", "monitor", "mousepad"], searchWord="mouse"),
                [["mobile", "moneypot", "monitor"], ["mobile", "moneypot", "monitor"], ["mouse", "mousepad"],
                 ["mouse", "mousepad"], ["mouse", "mousepad"]],
        ),
        (
                dict(products=["havana"], searchWord="havana"),
                [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]],
        ),
        # my checks
        (
                dict(products=["a", "b", "c"], searchWord="ab"),
                [["a"], []],
        ),
        (
                dict(products=["ab", "ba", "c"], searchWord="a"),
                [["ab"]],
        ),
        (
                dict(products=["ab", "ba", "c"], searchWord="ab"),
                [["ab"], ["ab"]],
        ),
        (
                dict(products=["abb", "aba", "ab"], searchWord="ab"),
                [["ab", "aba", "abb"], ["ab", "aba", "abb"]],
        ),
    ],
)
def test_solution(input_data, output):
    assert output == instance.suggestedProducts(**input_data)
