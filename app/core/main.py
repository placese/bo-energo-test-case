from fastapi import FastAPI

from api.routers import equations, colored_items


app = FastAPI()

app.include_router(
    equations.router,
    prefix="/equations",
)

app.include_router(
    colored_items.router,
    prefix="/colored_items",
)

