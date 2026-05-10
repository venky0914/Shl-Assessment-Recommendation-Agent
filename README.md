# SHL Assessment Recommendation Agent

An AI powered recommendation system that helps users find relevant SHL assessments based on job role or skill related queries.

This project scrapes assessment data from the SHL product catalog, creates semantic embeddings using Sentence Transformers, stores them in a FAISS vector database, and exposes a FastAPI endpoint for intelligent assessment recommendations.

---

# Features

- SHL product catalog scraping
- Clean dataset generation
- Semantic search using embeddings
- FAISS vector similarity search
- FastAPI REST API
- Swagger UI testing support
- Intelligent assessment recommendations

---

# Tech Stack

- Python
- FastAPI
- FAISS
- Sentence Transformers
- Pandas
- BeautifulSoup
- Requests
- Uvicorn

---

# Project Structure

```text
shl-assessment-agent/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── agent.py
│   ├── retriever.py
│   ├── models.py
│   ├── prompts.py
│   └── utils.py
│
├── scraper/
│   └── scrape_catalog.py
│
├── data/
│   ├── shl_catalog.csv
│   ├── faiss_index.index
│   └── metadata.pkl
│
├── evaluation/
│
├── requirements.txt
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone <your-github-repository-link>
cd shl-assessment-agent
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running The Project

## Step 1: Scrape SHL Catalog

```bash
python scraper/scrape_catalog.py
```

This creates:

- `data/shl_catalog.csv`

---

## Step 2: Create Embeddings and FAISS Index

```bash
python app/retriever.py
```

This creates:

- `data/faiss_index.index`
- `data/metadata.pkl`

---

## Step 3: Start FastAPI Server

```bash
uvicorn app.main:app --reload
```

Server will start at:

```text
http://127.0.0.1:8000
```

---

# API Documentation

After starting the server, open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI can be used to test the API endpoints.

---

# Chat Endpoint

## Endpoint

```http
POST /chat
```

## Sample Request

```json
{
  "messages": [
    {
      "role": "user",
      "content": "Java backend developer"
    }
  ]
}
```

---

# Sample Response

```json
{
  "reply": "I found 5 relevant SHL assessments.",
  "recommendations": [
    {
      "name": ".NET MVC (New)",
      "url": "https://www.shl.com/products/product-catalog/view/net-mvc-new/",
      "test_type": "K"
    }
  ],
  "end_of_conversation": false
}
```

---

# Health Check Endpoint

## Endpoint

```http
GET /health
```

## Response

```json
{
  "status": "ok"
}
```

---

# How It Works

1. Product catalog pages are scraped from SHL
2. Clean assessment descriptions are extracted
3. Sentence embeddings are generated using Sentence Transformers
4. FAISS stores vector embeddings for similarity search
5. User queries are converted into embeddings
6. Most relevant assessments are retrieved using semantic similarity

---

# Future Improvements

- Add larger SHL dataset coverage
- Improve assessment filtering
- Add frontend UI
- Deploy on Render or Railway
- Add conversation memory
- Add LLM based recommendation explanations

---

# Author

Venkateshwar Bommideni

---
