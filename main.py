from fastapi import FastAPI
from app.routes import ocr

app = FastAPI(title="DevBoard OCR+")

app.include_router(ocr.router, prefix="/ocr")
