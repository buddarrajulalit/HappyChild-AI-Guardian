from fastapi import APIRouter
from models.text_model import analyze_text
from routes.sse_routes import push_alert
router = APIRouter()
@router.post('/')
def text_analysis(payload: dict):
    content = payload.get('content', '')
    result = analyze_text(content)
    if result and 'toxic' in str(result[0]['label']).lower():
        push_alert(f'⚠️ Suspicious text detected: {content}')
    return {'input': content, 'analysis': result}
