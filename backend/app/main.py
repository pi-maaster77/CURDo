from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routres.elementos.router import router as elementos_router
from app.routres.tags.router import router as tags_router

app = FastAPI(
    title="CURDo API",
    version="0.2.0",
)

origins = [
"http://localhost:8080",]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(elementos_router, prefix="/api/elementos")
app.include_router(tags_router, prefix="/api/tags")  # Added router for tags