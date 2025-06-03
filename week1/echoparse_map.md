What each main .py file does (1 sentence per file)
What external APIs you call (Google Play, Apple, your LLM API)
What data flows in and out (reviews → processed data → frontend)
Draw a simple text diagram of: User Request → Backend → APIs → Database → Frontend

# Document Tree

```
root
├── echoparse-ui
│   ├── node_modules
│   ├── src
│       ├── AuthWrapper.jsx
│       ├── EchoparseUI.jsx
│       ├── LoginForm.jsx
│       ├── index.css
│       ├── main.jsx
│       ├── suabaseClient.js
│       ├── .env
│       ├── index.html
│       ├── package-lock.json
│       ├── postcss.config.js
│       ├── tailwind.config.js
├── .dockerignore 
├── .env.example
├── .gitignore
├── Dockerfile.fly
├── README.md
├── apple_reviews.csv
├── echoparse-ui.zip
├── echoparse_api.py
├── embed_and_upload_reviews.py
├── google_reviews.py
├── query_mixtral.py
├── requirements.txt
├── retrieve_reviews.py
├── scraper_apple_refactored.py
├── scraper_google_refactored.py
├── sql_vector_search.py
```

# Python File Responsibilities

| File                          | Description |
|-------------------------------|-------------|
| `echoparse_api.py`            | Main FastAPI backend exposing `/answer` and `/dashboard-metrics`. |
| `embed_and_upload_reviews.py` | Loads CSVs, computes embeddings, and inserts review data into Supabase. |
| `google_reviews.py`           | Legacy or alternate Google scraper (currently unused). |
| `query_mixtral.py`            | Contains logic for querying the Mixtral LLM with embedded prompts. |
| `retrieve_reviews.py`         | Used to retrieve review data from Supabase (legacy or utility). |
| `scraper_apple_refactored.py` | Scrapes Apple App Store reviews and writes to CSV. |
| `scraper_google_refactored.py`| Scrapes Google Play Store reviews and writes to CSV. |
| `sql_vector_search.py`        | Defines SQL logic for performing vector similarity search. |

---

# External APIs Used

| Service             | Purpose |
|---------------------|---------|
| **Google Play Scraper (via `google_play_scraper`)** | Live ratings + review text |
| **Apple iTunes RSS API** | Review data + ratings |
| **Together.ai API** | LLM completions (Mixtral 8x7B) for summarizing user questions |
| **Supabase REST API** | Stores embedded reviews for vector search |
| **SentenceTransformers** | Generates vector embeddings for user questions and reviews |

---

# Data Flow Overview

```
User
↓
Frontend (Vercel)
↓
FastAPI Backend (Render/Fly)
↓
┌─────────────┬──────────────────────────────┐
│ Scrapers │ ──> CSVs ──> Upload to DB │
│ │ (Google / Apple) │
└─────────────┴──────────────────────────────┘
↓
Supabase Vector DB
↓
Together LLM (answer synthesis)
↓
Frontend Response
```
