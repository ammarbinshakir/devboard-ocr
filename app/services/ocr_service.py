import os
import pytesseract
from PIL import Image
import io
import re
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set path to tesseract from .env
pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_PATH")


async def extract_text_and_tasks(file):
    image = Image.open(io.BytesIO(await file.read()))
    text = pytesseract.image_to_string(image)

    todos = re.findall(
        r"(?:fix|review|test|write|refactor)[^\n]+", text, re.IGNORECASE)
    pr_refs = re.findall(r"PR\s?#?\d+", text, re.IGNORECASE)
    dates = re.findall(r"\b(?:\d{1,2}[/-])?\d{1,2}[/-]\d{2,4}\b", text)

    return {
        "text": text,
        "todos": [t.strip() for t in todos],
        "refs": pr_refs,
        "dates": dates
    }
