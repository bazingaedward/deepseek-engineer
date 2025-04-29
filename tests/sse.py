from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio
from datetime import datetime

app = FastAPI()

async def event_generator():
    """生成 SSE 事件的异步生成器。"""
    while True:
        now = datetime.now().isoformat()
        yield f"data: Server time: {now}\n\n"
        await asyncio.sleep(1)  # 每秒发送一次事件

@app.get("/events")
async def events():
    """SSE 事件流的路由。"""
    return StreamingResponse(event_generator(), media_type="text/event-stream")