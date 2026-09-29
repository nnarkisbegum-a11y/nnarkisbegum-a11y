import os
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Static files mount
static_path = os.path.join(BASE_DIR, "static")
if os.path.exists(static_path):
    app.mount("/static", StaticFiles(directory=static_path), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    index_path = os.path.join(BASE_DIR, "templates", "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return "<h1>EduGenie App</h1><p>index.html file templates folder-il இல்லை!</p>"