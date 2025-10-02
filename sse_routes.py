from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import asyncio
import random

router = APIRouter()

# Queue for manual alerts
alerts_queue = []

# Example auto messages
alert_messages = [
    "🚨 Suspicious activity detected!",
    "⚠️ Warning: Content flagged.",
    "🔔 AI Guardian monitoring.",
    "🛡️ Safety check passed.",
    "📢 Harmful content detected.",
    "✅ System OK.",
    "🔍 Monitoring safe content.",
    "❗ Immediate action required.",
]

async def event_generator():
    count = 0
    while True:
        # Send manual alerts first (if any)
        if alerts_queue:
            alert = alerts_queue.pop(0)
            yield f"data: Manual Alert - {alert}\n\n"
        else:
            # Otherwise send auto alerts
            message = random.choice(alert_messages)
            count += 1
            yield f"data: Auto Alert {count} - {message}\n\n"

        await asyncio.sleep(2)

@router.get("/")
async def sse_alerts():
    return StreamingResponse(event_generator(), media_type="text/event-stream")

# Allow other routes to push alerts
def push_alert(message: str):
    alerts_queue.append(message)

