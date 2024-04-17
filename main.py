from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

app = FastAPI()


@app.get("/test", response_class=ORJSONResponse)
async def root():
    return {"operation": "ok"}
