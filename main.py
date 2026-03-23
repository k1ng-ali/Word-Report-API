from fastapi import FastAPI
from api.report import router as report_router
import stanza
#stanza.download('ru')
app = FastAPI()

app.include_router(report_router)

@app.get("/")
async def root():
    return {"status": "ok"}

