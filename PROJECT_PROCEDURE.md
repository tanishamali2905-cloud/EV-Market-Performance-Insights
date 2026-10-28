# End-to-End Project Procedure

1. **Collect data:** keep the supplied CSV in `data/ev_market_data.csv`; document its source/license if required.
2. **Prepare data:** run `python src/ev_analysis.py`. Inspect `outputs/dataset_profile.txt`, missing values, duplicates, field types, and out-of-range values. Review `outputs/count_distinct.csv` for distinct/null counts.
3. **Analyze:** use generated summary CSVs and charts; explain findings as observations from this supplied dataset only.
4. **Build Tableau sheets:** follow `tableau/TABLEAU_PROCEDURE.md` to create KPIs, category/manufacturer charts, ratings, trend, battery, and geography views.
5. **Dashboard:** arrange KPI cards, charts, and filters; test readability and filter behavior.
6. **Story:** create multiple scenes with captions supported by the data.
7. **Publish:** publish to Tableau Public only if permitted; open the link in another browser to verify it.
8. **Optional Flask:** replace the placeholder in `web_app/app.py` with your published Tableau URL, then run `python web_app/app.py`. Flask embeds a view but does not publish Tableau content.
9. **Demo:** record your actual Tableau dashboard/story and explain filters and findings. A visual mockup is not a substitute for the live workbook.
10. **GitHub:** extract the ZIP and upload its contents (folders/files), not just the ZIP.
