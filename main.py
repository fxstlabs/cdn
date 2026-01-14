from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.staticfiles import StaticFiles
from typing import Annotated

from starlette.responses import HTMLResponse

app = FastAPI()


@app.get("/status")
def status():
   return {
       "status": 200,
       "message": "ok"
   }

app.mount("/static", StaticFiles(directory="static"), name="static")