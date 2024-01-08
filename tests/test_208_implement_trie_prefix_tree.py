import pytest

from solutions.problem_208_implement_trie_prefix_tree import Trie


@pytest.mark.parametrize(
    'input_commands, input_values, expected',
    [
        (
            ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
            [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
            [None, None, True, False, True, None, True],
        ),
        # my checks
    ],
)
def test_solution(input_commands, input_values, expected):
    instance = None
    actual = []
    for command, value in zip(input_commands, input_values):
        match command:
            case "Trie":
                instance = Trie()
                actual.append(None)
            case "insert":
                actual.append(instance.insert(*value))
            case "search":
                actual.append(instance.search(*value))
            case "startsWith":
                actual.append(instance.startsWith(*value))
    assert actual == expected
