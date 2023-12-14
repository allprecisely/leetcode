import pytest

from solutions.problem_735_asteroid_collision import Solution

instance = Solution()


@pytest.mark.parametrize(
    'input, output',
    [
        (dict(asteroids = [5,10,-5]), [5, 10]),
        (dict(asteroids = [8,-8]), []),
        (dict(asteroids = [10,2,-5]), [10]),
        # my checks
        (dict(asteroids = [1]), [1]),
        (dict(asteroids = [-1]), [-1]),
        (dict(asteroids = [1, 2, 3]), [1, 2, 3]),
        (dict(asteroids = [-3, -2, -1, 1, 2, 3]), [-3, -2, -1, 1, 2, 3]),
        (dict(asteroids = [10, -11]), [-11]),
        (dict(asteroids = [10, -9]), [10]),
        (dict(asteroids = [-2, 10]), [-2, 10]),
        (dict(asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, -10]), [-10]),
        (dict(asteroids = [1, 2, 3, 4, 5, 6, 7, 8, 9, -9]), [1, 2, 3, 4, 5, 6, 7, 8]),


    ],
)
def test_solution(input, output):
    assert output == instance.asteroidCollision(**input)
