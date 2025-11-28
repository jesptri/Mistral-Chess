from mistralai import Mistral
from app.core.settings import settings
from app.core.pgn_parser import STORE

client = Mistral(api_key=settings.mistral_api_key)

def answer_question(question: str) -> str:
    """
    Answer a question about indexed PGN games.
    
    Args:
        question: User question in normal humanlanguage
        
    Returns:
        AI-generated answer
    """
    if not STORE:
        return "No documents shared yet. Please upload a PGN file first."
    
    context_parts = []
    for doc_id, doc in STORE.items():
        context_parts.append(f"""
            Chess Game:
            - Event: {doc['event']}
            - White: {doc['white']} (Elo: {doc['white_elo']})
            - Black: {doc['black']} (Elo: {doc['black_elo']})
            - Result: {doc['result']}
            - Date: {doc['date']}
            - Site: {doc['site']}

            Moves:
            {doc['moves']}
            """)
    
    full_context = "\n\n---\n\n".join(context_parts)
    
    prompt = f"""
    You are a chess expert having a strong experience in analyzing chess positions, either in opening, middlegame or endgame. 
    Here are chess games in PGN format.

    {full_context}

    User question: {question}

    Answer precisely by analyzing the moves and metadata. 
    - If the input is not about the chess games (if it is like "Hello", "How are you?", "What is the weather?", "What is the time?", etc.), say "I'm sorry, I can only answer questions about chess games."
    - If the question is about tactics or strategy, make sure to analyze in depth the position (you can take your time!). You should have analyzed the full game, not just the last moves to give insight about the game. If referencing specific moves, cite them."""
    
    # Call Mistral directly
    try:
        response = client.chat.complete(
            model="mistral-small-latest",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling Mistral API: {str(e)}\n\nRaw context:\n{full_context}"

