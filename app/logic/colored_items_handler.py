from schemas.colored_items import ColoredItemsBaseModel, Color
import random

async def predict_color(number: int) -> ColoredItemsBaseModel:
    """Функция, угадывающая цвет предмета
    Function for prediction color of item
    """
    result = random.choices(list(Color), weights=[60, 25, 15],  k=1)[0]
    print(f"{result=}")

    return ColoredItemsBaseModel(color=result)
    
