

from app import app 
from app import config
import os
import random
import string
from fastapi import UploadFile

def buildRandomString(size):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))


@app.get('/v1/file/delete', description='Удаление файла', tags=['File object'])
def deleteFile(url: str):
    os.remove(config.STATIC_FOLDER_URL+url.split('/')[-1])
    return '{"status":"ok"}'


@app.post('/v1/file/upload', description='Выгрузка файла', tags = ['File object'])
def uploadFile(file: UploadFile):
    filename = buildRandomString(30)+'.png'
    with open(config.STATIC_FOLDER_URL+filename, "wb+") as file_object:
        file_object.write(file.file.read())
    return config.MEDIA_SERVER_ADDRESS+filename