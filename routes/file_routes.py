from fastapi import APIRouter, UploadFile, File
from domain.file_processor import FileProcessor


router = APIRouter()

@router.post("/file/create_file")
async def create_file():
    return FileProcessor().create_file()

@router.post("/upload_file/")
async def uploadFile(file:UploadFile = File(...)):
    return await FileProcessor().upload_file(file)

@router.post("/file/add_data/")
async def add_data(conta: str, agencia: str, texto:str, valor:float):
    data = {'conta':conta, "agencia":agencia, "texto":texto, "valor":valor}
    return await FileProcessor().add_data_to_file(data)

@router.get("/file/file_list")
async def file_list():
    return await FileProcessor().list_file()

@router.get("/file/delete")
async def delete_data():
    return{"message": "Lista de dados"}