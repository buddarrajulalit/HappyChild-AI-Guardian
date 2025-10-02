from fastapi import FastAPI
from routes import text_routes, image_routes, audio_routes, sse_routes

app = FastAPI(title="HappyChild - AI Guardian")

# Register routers
app.include_router(text_routes.router, prefix="/analyze/text")
app.include_router(image_routes.router, prefix="/analyze/image")
app.include_router(audio_routes.router, prefix="/analyze/audio")
app.include_router(sse_routes.router, prefix="/alerts")

@app.get("/")
def root():
    return {"message": "HappyChild API running!"}
