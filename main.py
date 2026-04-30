from fastapi import FastAPI
from api.routes import health, movimentacoes
from core.database import engine, Base
from models.movimentacao import Movimentacao
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

#Base.metadata.create_all(bind=engine)

app = FastAPI(title="Missão 2", lifespan=lifespan)

#app.include_router(health_router)

app.include_router(health.router, prefix="/health", tags=["Health"])
app.include_router(movimentacoes.router, prefix="/movimentacoes", tags=["Movimentações"])