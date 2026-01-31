from fastapi import FastAPI
import uvicorn
from database import engine
from models.user import User
from models.product import Product
from routers.user import router as user_router
from routers.product import router as product_router
from routers.authentication import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager



@asynccontextmanager
async def lifespan(app: FastAPI):
    # on startup
    create_db_tables()
    yield
    # on shutdown


app = FastAPI(title="Fastapi boilerplate for open-source", lifespan=lifespan)


app.include_router(auth_router)
app.include_router(user_router)
app.include_router(product_router)

origins = '*'

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def create_db_tables():
    User.metadata.create_all(engine)
    Product.metadata.create_all(engine)


@app.get('/')
async def home():
    return {"Home Page!"}


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True)