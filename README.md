# Cardano Transaction Analysis

This app gets transactions from cardanoscan.io and analyses them

# Run:
```
poetry install
poetry shell
cd src
poetry run uvicorn main:app --reload
```

## Todo:

- [x] Create basic scraper
- [x] Get individual transactions
- [ ] Parse data and output json with all relevant data
- [ ] Output REST with specific route ex. /transaction/hash/total_fees
- [ ] Set up BigQuery to analyze whole blockchain
