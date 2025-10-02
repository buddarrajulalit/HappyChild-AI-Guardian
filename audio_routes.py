from fastapi import APIRouter, UploadFile, File
import shutil, os
from models.audio_model import analyze_audio
from routes.sse_routes import push_alert
router = APIRouter()
@router.post('/')
def audio_analysis(file: UploadFile = File(...)):
    save_path = f'static/{file.filename}'
    with open(save_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    result = analyze_audio(save_path)
    transcript = result.get('text', '')
    keywords = ['secret', 'danger', 'meet']
    if any(word in transcript.lower() for word in keywords):
        push_alert(f'⚠️ Suspicious audio detected: {transcript}')
    os.remove(save_path)
    return {'filename': file.filename, 'analysis': result}
