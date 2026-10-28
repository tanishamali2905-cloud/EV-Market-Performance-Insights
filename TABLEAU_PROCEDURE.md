# Tableau Dashboard and Story Procedure

## 1. Connect CSV
Open Tableau Public/Desktop → Connect → Text File → choose `data/ev_market_data.csv`. Check field types and open Sheet 1.

## 2. Create KPI calculated fields
In Data pane, right-click → Create Calculated Field. Use the exact field names in Tableau:

| KPI | Formula |
|---|---|
| Total Manufacturers | `COUNTD([manufacturer])` |
| Total EV Models | `COUNTD([vehicle_id])` |
| Total Annual EV Sales | `SUM([annual_sales_units])` |
| Average Customer Rating | `AVG([customer_rating])` |
| Average Driving Range | `AVG([range_km])` |
| Average Battery Capacity | `AVG([battery_capacity_kwh])` |

For each KPI, drag the field to Text on the Marks card. If your column names differ, use the names shown in the Data pane.

## 3. Worksheets
- Category sales: `category` → Columns; `annual_sales_units` → Rows as SUM; sort descending.
- Manufacturer comparison: `manufacturer` → Rows; annual sales → Columns; sort descending; optionally filter Top 10.
- Ratings: category and AVG(customer_rating).
- Sales trend: if `model_year` exists, put it on Columns and SUM(annual_sales_units) on Rows.
- Battery distribution: battery_type with record count or sales; sorted bar chart is a clear choice.
- Geographic distribution: use manufacturing_country or market_region; set geographic role if recognized, otherwise use a bar chart.
- Price/range: histogram of price_usd; scatter plot of battery_capacity_kwh vs range_km.

## 4. Filters and dashboard
Add filters for manufacturing_country, manufacturer, category; choose Show Filter. Create a dashboard titled **EV Market Performance & Insights**. Put KPI cards at top, charts below, and filters along the left/top. Test filters and chart actions.

## 5. Story scenes
Click New Story and add a view/dashboard to each point. Suggested scenes: (1) EV Market at a Glance, (2) Category Distribution, (3) Leading Manufacturers, (4) Customer Ratings, (5) Annual Sales Trend, (6) Battery Technology, (7) Global Manufacturing Footprint, (8) Key Insights. Write captions based on actual results, then save and publish if required. Test the published URL and record the real dashboard/story for your demo.
