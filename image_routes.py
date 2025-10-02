from fastapi import APIRouter, UploadFile, File
import shutil, os
from models.image_model import analyze_image
from routes.sse_routes import push_alert
router = APIRouter()
@router.post('/')
def image_analysis(file: UploadFile = File(...)):
    save_path = f'static/{file.filename}'
    with open(save_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    result = analyze_image(save_path)
    if result['width'] > 1000 or result['height'] > 1000:
        push_alert(f'⚠️ Suspicious image detected: {file.filename}')
    os.remove(save_path)
    return {'filename': file.filename, 'analysis': result}
