from fastapi import APIRouter, UploadFile, File
from domain.file_processor import FileProcessor


router = APIRouter()

@router.post("/file/create_file")
async def create_file():
    return FileProcessor().create_file()

@router.post("/upload_file/")
async def uploadFile(file:UploadFile = File()):
    return await FileProcessor.upload_file()

@router.delete("/file/delete_data")
async def delete_data():
    return{"message": "Dado removido com sucesso"}

@router.get("/file/list_file")
async def delete_data():
    return{"message": "Lista de dados"}