import pytest

from solutions.problem_739_daily_temperatures import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input_data, output',
    [
        (dict(temperatures = [73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0]),
        (dict(temperatures = [30,40,50,60]), [1,1,1,0]),
        (dict(temperatures = [30,60,90]), [1,1,0]),
        # my checks
        (dict(temperatures=[30, 30, 30]), [0, 0, 0]),
        (dict(temperatures=[40, 35, 30]), [0, 0, 0]),
        (dict(temperatures=[40, 35, 50]), [2, 1, 0]),

    ],
)
def test_solution(input_data, output):
    assert output == instance.dailyTemperatures(**input_data)
