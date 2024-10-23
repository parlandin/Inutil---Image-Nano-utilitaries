from rembg import remove
from PIL import Image
from io import BytesIO

async def process_image(file):
    # Abrir a imagem a partir do arquivo enviado
    input_image = Image.open(BytesIO(await file.read()))
    
    # Remover o fundo da imagem
    output_image = remove(input_image, post_process_mask=True)

    # Salvar a imagem em um buffer de bytes
    img_io = BytesIO()
    output_image.save(img_io, 'PNG')
    img_io.seek(0)

    return img_io
