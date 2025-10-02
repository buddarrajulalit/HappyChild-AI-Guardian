import whisper
model = whisper.load_model('small')
def analyze_audio(file_path: str):
    result = model.transcribe(file_path)
    return result
