# Week 2: Review Scraping & Pandas Fundamentals

## ✅ Goals for the Week
- Scrape Apple App Store reviews (✅ done)
- Clean and format review data with Pandas
- Explore data with basic analysis and plots
- Sketch and document the scraper → transform → store pipeline

---

### 🟩 Monday (Completed)

- Refactored Apple scraper (`scraper_app_store.py`)
- Loop through pages, extract review fields, write to `data.csv`
- Clear separation: the script scrapes only; no data formatting

---

### 🟨 Tuesday (Today)

1. Load `data.csv` into Pandas DataFrame  
2. Clean and format:
   - Convert `rating` to `float`
   - Parse `review_date` as datetime (ISO 8601)
   - Strip whitespace; handle missing/null values  
3. Explore data:
   - Count of total reviews
   - Average rating
   - Plot histogram of ratings  
4. (Optional) Discuss pipeline structure: where scraper ends, transformer begins

---

### 🟦 Wednesday

- Aggegation & Grouping:
  - Reviews per day or rating
  - Rating distribution
  - Plot using Pandas `.plot(kind="bar")`

---

### 🟪 Thursday

- Add columns:
  - `review_length` (word count)
  - `review_year` from `date`  
- Create `pipeline_diagram.md` sketch: scraper → cleaner → database/store

---

### 🔷 Friday

- Finalize repo structure under `week02/`
- Write `README.md` explaining:
  - What we scraped
  - How we processed it
  - What insights we gained
- Commit & push to GitHub

---

### 🧭 Weekend Project

- Build a Google Play Store review scraper:
  - Model after Apple scraper
  - Optional: export cleaned data to `.parquet`

---

### 🎧 Listening
- *Talk Python to Me*: Web Scraping at Scale  
- *Practical AI*: Scraping, Parsing, & Cleaning Real Data

### 📐 Daily Math (5 min)
- Khan Academy: Introduction to Scatter Plots & Correlation
