from typing import NamedTuple
from math import sqrt


class RootsOfQuadraticEquation(NamedTuple):
    x1: float | None = None
    x2: float | None = None


class NonQuadraticEquationError(Exception):
    pass


async def solve_quadratic_equation(a: float,
                             b: float = 0.0,
                             c: float = 0.0) -> RootsOfQuadraticEquation:
    """Функция решения квадратного уравнения
    Quadratic equation solve funciton 
    """
    if a == 0:
        raise NonQuadraticEquationError("Parameter a should not be null or 0")
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return RootsOfQuadraticEquation()
    elif discriminant == 0:
        x = -b / (2 * a)
        return RootsOfQuadraticEquation(x1=x, x2=x)
    x1 = (-b + sqrt(discriminant)) / (2 * a)
    x2 = (-b - sqrt(discriminant)) / (2 * a)
    return RootsOfQuadraticEquation(x1=x1, x2=x2)

