# Applied Analytics Mini Project

A beginner-friendly project demonstrating ETL, SQLite, parameterized SQL queries, and testing.

## Project Structure
```
vibe-kpi-demo/
├── data/
│   ├── raw/
│   │   └── customers_raw.csv      # Sample customer data
│   └── db/
│       └── analytics.db           # SQLite database (created by ETL)
├── src/
│   ├── etl_load_sqlite.py         # ETL script to load CSV into SQLite
│   └── kpi_city.py                # KPI script with parameterized SQL
├── tests/
│   └── test_kpi_city.py           # Pytest tests for KPI script
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

## Setup & Run Commands

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run ETL to load CSV into SQLite:**
   ```bash
   python src/etl_load_sqlite.py
   ```

3. **Run KPI script (demonstrates SQL injection protection):**
   ```bash
   python src/kpi_city.py
   ```

4. **Run tests:**
   ```bash
   pytest tests/test_kpi_city.py
   ```

## Key Concepts
- **ETL**: Extract (CSV) → Transform (pandas) → Load (SQLite)
- **Parameterized SQL**: Prevents SQL injection attacks using `?` placeholders
- **Testing**: Pytest for validating code behavior
