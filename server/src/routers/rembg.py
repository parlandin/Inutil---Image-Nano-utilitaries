from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from services.rembg_service import process_image
from io import BytesIO

router = APIRouter()

@router.post("/bg/basic/upload/")
async def upload_file(file: UploadFile = File(...)):
    print("Recebendo arquivo...")
    if file.filename == "":
        raise HTTPException(status_code=400, detail="No file selected")
    
    try:
        # Processar a imagem e remover o fundo
        img_io = await process_image(file)

        print("Imagem processada com sucesso!")
        # Retornar a imagem processada como download
        return StreamingResponse(img_io, media_type="image/png", headers={"Content-Disposition": "attachment; filename=_rmbg.png"})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
