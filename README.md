# EV Market Performance & Insights

A beginner-friendly project analyzing EV categories, manufacturers, sales, price, driving range, battery technology, customer ratings, and regions.

## Contents
- `data/ev_market_data.csv` — supplied dataset.
- `src/ev_analysis.py` — runnable Python analysis, count-distinct summary, and chart generation.
- `outputs/` — generated profile, summary CSVs, and charts.
- `tableau/TABLEAU_PROCEDURE.md` — instructions to create a Tableau dashboard and Story.
- `docs/PROJECT_PROCEDURE.md` — end-to-end project procedure.
- `web_app/app.py` — optional Flask page for embedding a published Tableau view.
- `requirements.txt` — Python dependencies.

## Run
Install Python 3.10+, then run:
```bash
pip install -r requirements.txt
python src/ev_analysis.py
```

The analysis describes this supplied dataset only; do not present it as verified official market statistics unless you verify the original source. A finished Tableau workbook is not included: create and test it in Tableau using the steps in `tableau/TABLEAU_PROCEDURE.md`.
