# End-to-End Data Engineering Project: FMCG Sales Data

This project implements a complete local Data Engineering pipeline based on the **Medallion Architecture**, simulating Fast-Moving Consumer Goods (FMCG) sales data flows. It runs locally using Python and is orchestrated to cleanly move data through several refinement stages.

## Medallion Architecture

The concept is to ingest data into raw states, clean/standardize it, and finally produce business-ready wide tables.

1. **Landing Zone (`data/Landing`)**: Mock generation of dirty, unformatted CSV records (`customers`, `products`, `orders`). Emulates drop-in data lakes.
2. **Bronze Layer (`data/Bronze`)**: Appends audit properties (`_ingestion_timestamp`) to the raw records. Saved as `.parquet` files for efficiency.
3. **Silver Layer (`data/Silver`)**: Data enrichment and standardization. This involves stripping whitespace, fixing known spelling errors with dictionaries, formatting datetimes correctly, and deriving features (such as hashing Product IDs and extracting text variants with Regex).
4. **Gold Layer (`data/Gold`)**: Merging operational data sources. The Facts (`fact_orders`) and Dimensions (`dim_customers`, `dim_products`) are merged into a final "Wide Table", adding business calculables like `revenue`. Exported both as a `.csv` for Excel/Tableau users and a modernized `.parquet`.

## Project Structure

```bash
.
├── pyproject.toml              # Project dependencies (managed by uv)
├── main.py                     # Main execution orchestrator
├── README.md                 
├── src/                        # Modular pipeline components
│   ├── utils/
│   │   └── config.py           # Core variables and folder configurations
│   ├── pipeline/
│   │   ├── generate_data.py    # Generates mock scenarios into Landing
│   │   ├── bronze.py           # Loads Landing to Bronze (auditing)
│   │   ├── silver.py           # Cleanses Bronze data to Silver
│   │   └── gold.py             # Joins tables and computes derived metrics
│   └── analytics/
│       └── duckdb_queries.py   # Final aggregate analytical reporting
└── data/                       # Directory populated by pipeline
    ├── Landing/
    ├── Bronze/
    ├── Silver/
    └── Gold/
```

## Running the Pipeline

This project uses `uv` as the package manager and test runner.

1. Install dependencies and run the whole orchestrator immediately by executing:

```bash
uv run .\main.py
```

2. After executing, the program will create the corresponding folder structures within `/data` and populate the Medallion layers up to analytical tables. An analytical summary will be outputted to your terminal using DuckDB.

## Analytics Highlights

The analysis relies on the ultra-fast DuckDB engine executing SQL queries dynamically against our `Gold` Parquet exports. Key metrics currently include:
* **Total Revenue by City**: Summarizing aggregated sales numbers grouped by demographic mappings.
* **Category-Based Sales**: Measuring overall quantity sold against arbitrary products alongside average basket amounts.
