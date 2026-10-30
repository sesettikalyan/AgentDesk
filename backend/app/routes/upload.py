from fastapi import APIRouter, UploadFile, HTTPException
import shutil

from app.services.pdf_service import extract_pdf_info

router = APIRouter()


@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        pdf_info = extract_pdf_info(file_path)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error))

    return {
    "filename": file.filename,
    "pages": pdf_info["pages"],
    "characters": pdf_info["characters"],
    "chunks": pdf_info["chunks"],
    "embedding_count": pdf_info["embedding_count"],
    "embedding_dimension": pdf_info["embedding_dimension"],
    "stored_in_chromadb": pdf_info["stored_in_chromadb"]

}                  



