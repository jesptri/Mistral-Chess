from fastapi import APIRouter, UploadFile, File, HTTPException
from app.core.pgn_parser import index_pgn
import pathlib

router = APIRouter()

@router.post("/", summary="Upload and index a PGN file")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(('.pgn', '.txt')):
        raise HTTPException(status_code=400, detail="Only .pgn or .txt files supported.")
    
    content = await file.read()
    doc_id, meta = index_pgn(file.filename, content)
    return {"document_id": doc_id, "meta": meta}

@router.post("/demo", summary="Load the demo PGN file")
async def load_demo_file():
    demo_path = pathlib.Path(__file__).parent.parent / "demo_files" / "Mazzella-Espinoux.pgn"
    
    try:
        with open(demo_path, 'rb') as f:
            content = f.read()
        
        doc_id, meta = index_pgn("Mazzella-Espinoux.pgn", content)
        return {"document_id": doc_id, "meta": meta, "source": "demo"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing demo file: {str(e)}")
