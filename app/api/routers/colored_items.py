from fastapi import APIRouter, HTTPException

from schemas.colored_items import ColoredItemsBaseModel
from logic.colored_items_handler import predict_color


router = APIRouter()

@router.get("/", response_model=ColoredItemsBaseModel)
async def get_color(number: int):
    if number < 1 or number > 100:
        raise HTTPException(status_code=400,
                detail="Number should be from 1 to 100")
    result = await predict_color(number)
    return result

