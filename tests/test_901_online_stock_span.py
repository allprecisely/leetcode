import pytest

from solutions.problem_901_online_stock_span import StockSpanner


@pytest.mark.parametrize(
    'input_commands, input_values, expected',
    [
        (
            ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"],
            [[], [100], [80], [60], [70], [60], [75], [85]],
            [None, 1, 1, 1, 2, 1, 4, 6],
        ),
        # my checks
        (
            ["StockSpanner"],
            [[]],
            [None],
        ),
        (
            ["StockSpanner", "next"],
            [[], [10]],
            [None, 1],
        ),
        (
            ["StockSpanner", "next", "next", "next"],
            [[], [10], [20], [30]],
            [None, 1, 2, 3],
        ),
    ],
)
def test_solution(input_commands, input_values, expected):
    instance = None
    actual = []
    for command, value in zip(input_commands, input_values):
        match command:
            case "StockSpanner":
                instance = StockSpanner()
                actual.append(None)
            case "next":
                actual.append(instance.next(*value))
    assert actual == expected
