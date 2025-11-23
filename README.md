# Mistral Chess

As a chess player, I found interesting to build the project around my passion !

I built an AI-powered chess game analysis application with FastAPI. 

Upload PGN files and ask questions about the games !

## Features

**Simple PGN Processing**: Upload standard chess PGN files from Chess.com, Lichess, or other platforms

**Direct LLM Context**: Leverages PGN's structured format (metadata + moves) for efficient analysis

**AI-Powered Q&A**: Ask questions about chess games and get intelligent answers

## Prerequisites

- Docker installed (recommended) **OR** Python 3.11+
- Mistral API Key (generate one at [console.mistral.ai](https://console.mistral.ai))

## Quick Start (Docker - Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jesptri/mistral-chess.git
   cd mistral-chess
   ```

2. **Build and run with Docker:**
   ```bash
   docker build -t mistral-chess-qa .
   docker run -p 8000:8000 -e MISTRAL_API_KEY="your-api-key-here" mistral-chess-qa
   ```

3. **Open your browser:**
   Navigate to [http://localhost:8000](http://localhost:8000)

## How It Works

1. **PGN Parsing**: Extract metadata (players, event, date) and moves using regex
2. **Storage**: Store structured data in memory
3. **Question Answering**: Send complete game context directly to Mistral LLM

**Why this approach?**
- PGN files have a very structured format: metadata at the top, moves following
- The LLM sees the complete context for better answers

## Project Structure

```
app/
├── api/
│   ├── documents.py           # PGN file upload endpoints
│   └── query.py               # Question answering endpoint
├── core/
│   ├── pgn_parser.py          # PGN parsing
│   ├── retrieval.py           # LLM question answering
│   └── settings.py            # Configuration
├── models/
│   └── schemas.py             # Data models
├── templates/
│   └── index.html             # Web interface
├── demo_files/
│   └── Mazzella-Espinoux.pgn  # Demo chess game, one of my best performances at the 2019 French Youth Championships
└── main.py
```

## Configuration

The application uses an environment variable:

- `MISTRAL_API_KEY`: Your Mistral API key (required)

## Alternative: Local Development (Without Docker)

If you prefer to run without Docker:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/jesptri/mistral-chess.git
   cd mistral-chess
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your Mistral API key in a .env file at the root:**
   ```bash
   MISTRAL_API_KEY="your-api-key-here"
   ```

4. **Run the server:**
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
   
   Or simply use:
   ```bash
   make run
   ```

5. **Open your browser:**
   Navigate to [http://localhost:8000](http://localhost:8000)