from fastapi import APIRouter
from app.models.schemas import QueryRequest, QueryResponse
from app.core.simple_retrieval import answer_question

router = APIRouter()

@router.post("/query/", response_model=QueryResponse)
def query(req: QueryRequest):
    answer = answer_question(req.question)
    return QueryResponse(answer=answer)
