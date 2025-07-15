from fastapi import APIRouter, UploadFile, File
from app.services.ocr_service import extract_text_and_tasks

router = APIRouter()


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    result = await extract_text_and_tasks(file)
    return result
