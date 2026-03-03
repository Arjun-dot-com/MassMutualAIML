from fastapi import FastAPI
from app.api import analyze
from app.core.config import settings  # <-- Import your settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="AI backend for analyzing student profiles and generating study plans."
)

app.include_router(analyze.router)

@app.get("/")
async def health_check():
    return {"status": "active", "service": settings.PROJECT_NAME}