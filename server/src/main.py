from fastapi import FastAPI
from routers import rembg

app = FastAPI()

# Incluir o roteador de upload de imagens
app.include_router(rembg.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
