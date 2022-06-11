from fastapi import APIRouter, HTTPException

from schemas.equations import QuadraticEquationBaseModel
from logic.equations_handler import (
        solve_quadratic_equation,
        NonQuadraticEquationError,
)


router = APIRouter()

@router.get("/quadratic_equation/", response_model=QuadraticEquationBaseModel)
async def quadratic_eqution(a: float, b: float = 0.0, c: float = 0.0):
    try:
        result = await solve_quadratic_equation(a, b, c)
        return result._asdict()
    except NonQuadraticEquationError as e:
        raise HTTPException(status_code=400, detail=f"{e}")


