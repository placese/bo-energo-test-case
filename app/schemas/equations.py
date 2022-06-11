from pydantic import BaseModel


class QuadraticEquationBaseModel(BaseModel):
    x1: float | None 
    x2: float | None 

