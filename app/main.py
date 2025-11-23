from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi import Request
from app.api import documents, query
from fastapi.middleware.cors import CORSMiddleware
import pathlib

app = FastAPI(title="Mistral Chess Q&A")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory=str(pathlib.Path(__file__).parent / "templates"))

app.include_router(documents.router, prefix="/documents", tags=["documents"])
app.include_router(query.router, prefix="/query", tags=["query"])

@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

@app.get('/health')
async def health():
    return {"status": "ok"}
