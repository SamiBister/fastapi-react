from fastapi import Depends, FastAPI



from app.internal import admin
from app.routers import users, items
from app.dependencies import get_token_header, get_query_token

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

@app.get("/back")
async def root():
    return {"message": "This is from backend !!!!"}
