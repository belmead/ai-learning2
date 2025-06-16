"""
embed.py

This script takes the cleaned CSV files and embeds on them.

1. Setup

    Import libraries (pandas, sentence_transformers)
    Define input CSV path and output CSV path

2. Load Cleaned Data

    Read CSV into a Pandas DataFrame
    Ensure review_text is present and non-null

3. Prepare Texts

    Prepend "passage: " to each entry in review_text (create new list or Series)

4. Load Model

    Load the intfloat/e5-base model using SentenceTransformer

5. Generate Embeddings

    Pass the prepared texts to model.encode()
    (Done in batches for speed and memory efficiency)

6. Store Results

    Add embeddings as a new column (embedding)
    Export to a new Parquet file (CSV may require serialization of the vectors) - Will do CSV after Parquet testing works
"""

import pandas as pd
import torch
from sentence_transformers import SentenceTransformer
import requests

"""
Use this for now on (but do not share)

openai_key = '18308dfb05604c0a9b0b3938df66f684'
openai_url = 'https://cacu-cog-dev.openai.azure.com/openai/deployments'
model = 'A1DVDTAOAI01-TEXT-EMBEDDING-ADA-002'
prompt_body = {'input': 'text to embed'}
embeddings = f'{openai_url}/{model}/embeddings?api-version=2023-08-01-preview'
response = requests.post(embeddings,
                            headers={'api-key': openai_key, 'Content-Type': 'application/json'},
                            json=prompt_body
                        )
"""
device = "cpu" # explicitly set the device

model = SentenceTransformer("intfloat/e5-mistral-7b-instruct", device=device) # embedder, cpu-only for the Macbook

google_df = pd.read_csv("clean_google_play.csv")
apple_df = pd.read_csv("clean_app_store.csv")

combined_frame = [google_df, apple_df]

result = pd.concat(combined_frame, ignore_index=True)

result["prepared_text"] = (
    "platform: " + result["platform"].astype(str) + ". " +
    "date: " + result["review_date"].astype(str) + ". " +
    "rating: " + result["rating"].astype(str) + ". " +
    "version: " + result["app_version"].astype(str) + ". " +
    "passage: " + result["review_text"].astype(str)
)

result["embedding"] = model.encode(result["prepared_text"].tolist(), batch_size=32, show_progress_bar=True).tolist() # use tolist() else it writes to a 2D matrix instead of the expected 1D shape

# to parquet for intermediate testing — supabase does not accept parquet, but we can turn it back into a csv later

result.to_parquet("embedded_reviews.parquet")