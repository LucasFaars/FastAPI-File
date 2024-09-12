import os
import csv
from fastapi.exceptions import HTTPException
from fastapi import status, UploadFile


class FileProcessor:
#Gestor de arquivos#
    def __init__(self):
        self.file_path = "data/seu_file.csv"
        self.directory = "data"

    def create_file(self):
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['conta','agencia', 'texto', 'valor'])
                return {'mensagem':f'Criado, {self.file_path}'}
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Sla')
    
    async def upload_file(self, file: UploadFile):
        if file.filename.endswith('.csv'):
            try:
                content = await file.read()
                decoded_file = content.decode("utf-8").splitlines()
                csv_reader = csv.DictReader(decoded_file)
                for row in csv_reader:
                    print(row)
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'message':f"Falha ao processar arquivo {file.filename}"})          
        else:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail={'message':f"Somende csv, n {file.filename}"})
        
    async def add_data_to_file(self,data:dict):
        if os.path.exists(self.file_path):
            with open(self.file_path, mode="a",newline="" )  as file:
                writer = csv.writer(file)
                writer.writerow([data['conta'], data['agencia'], data['texto'], data['valor']])
                return {"mensagem": f"Dados inseridos com sucesso: {data}"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Arquivo inexistente.")