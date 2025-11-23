"""
Simple PGN parser without external chess libraries.
Extracts metadata and moves directly from PGN format.
"""
import re
import uuid
from typing import Dict, Any, Tuple

# In-memory store for indexed PGN games
STORE: Dict[str, Dict[str, Any]] = {}


def parse_pgn(raw_bytes: bytes) -> Tuple[str, Dict[str, Any]]:
    """
    Parse PGN file by extracting metadata and moves.
    
    PGN format is simple:
    - Metadata: lines like [Key "Value"]
    - Moves: everything else after metadata
        
    Returns:
        (doc_id, document_data)
    """
    text = raw_bytes.decode('utf-8', errors='ignore')
    
    # Extract metadata
    metadata = {}
    for line in text.split('\n'):
        match = re.match(r'\[(\w+)\s+"([^"]+)"\]', line.strip())
        if match:
            key, value = match.groups()
            metadata[key] = value
    
    # Extract moves
    moves_text = re.sub(r'\[.*?\]', '', text).strip()
    moves_text = ' '.join(moves_text.split())
    
    # Structure the document
    doc_id = str(uuid.uuid4())
    document_data = {
        "id": doc_id,
        "metadata": metadata,
        "moves": moves_text,
        "white": metadata.get('White', 'N/A'),
        "black": metadata.get('Black', 'N/A'),
        "white_elo": metadata.get('WhiteElo', 'N/A'),
        "black_elo": metadata.get('BlackElo', 'N/A'),
        "result": metadata.get('Result', 'N/A'),
        "date": metadata.get('Date', 'N/A'),
        "event": metadata.get('Event', 'N/A'),
        "site": metadata.get('Site', 'N/A'),
    }
    
    return doc_id, document_data


def index_pgn(filename: str, raw_bytes: bytes) -> Tuple[str, Dict]:
    """
    Index a PGN file in the simple store.
        
    Returns:
        (doc_id, metadata_summary)
    """
    doc_id, data = parse_pgn(raw_bytes)
    data['filename'] = filename
    STORE[doc_id] = data
    
    return doc_id, {
        "filename": filename,
        "white": data['white'],
        "black": data['black'],
        "result": data['result'],
        "event": data['event']
    }

