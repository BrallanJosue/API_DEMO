
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/v1/conductos")
async def get_contactos():
    #TODO read contactos.csv
    #TODO JSON encode contactos.csv
    #TODO save in response
    response = []
    return response 
