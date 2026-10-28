"""Run from the repository root: python src/ev_analysis.py"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'ev_market_data.csv'
OUT = ROOT / 'outputs'; CHARTS = OUT / 'charts'
OUT.mkdir(exist_ok=True); CHARTS.mkdir(parents=True, exist_ok=True)
def col(df, options): return next((x for x in options if x in df.columns), None)
def chart(s, title, filename, horizontal=False, top=15):
    s = s.dropna().head(top)
    if s.empty: return
    fig, ax = plt.subplots(figsize=(10, 6))
    if horizontal: s.sort_values().plot(kind='barh', ax=ax)
    else: s.plot(kind='bar', ax=ax); ax.tick_params(axis='x', labelrotation=35)
    ax.set_title(title); ax.set_ylabel('Count / units'); fig.tight_layout()
    fig.savefig(CHARTS / filename, dpi=160); plt.close(fig)
def main():
    if not DATA.exists(): raise FileNotFoundError(f'Place CSV at {DATA}')
    df = pd.read_csv(DATA)
    profile = [f'Rows: {len(df):,}', f'Columns: {len(df.columns)}', f'Duplicates: {df.duplicated().sum():,}', f'Missing cells: {df.isna().sum().sum():,}', '', 'DATA TYPES', df.dtypes.to_string(), '', 'MISSING BY FIELD', df.isna().sum().sort_values(ascending=False).to_string(), '', 'NUMERIC SUMMARY', df.describe(include='number').T.to_string()]
    (OUT/'dataset_profile.txt').write_text('\n'.join(profile), encoding='utf-8')
    pd.DataFrame({'Field_Name':df.columns,'Distinct_Count':[int(df[x].nunique(dropna=True)) for x in df.columns],'Null_Count':[int(df[x].isna().sum()) for x in df.columns],'Tableau_Calculated_Field_Formula':[f'COUNTD([{x}])' for x in df.columns]}).to_csv(OUT/'count_distinct.csv', index=False)
    category=col(df,['category','vehicle_category','ev_category']); sales=col(df,['annual_sales_units','annual_sales','sales_units']); maker=col(df,['manufacturer','make','brand']); region=col(df,['market_region','region','manufacturing_country','country']); battery=col(df,['battery_type','battery_technology']); price=col(df,['price_usd','price','vehicle_price']); rng=col(df,['range_km','driving_range_km','range']); capacity=col(df,['battery_capacity_kwh','battery_capacity']); rating=col(df,['customer_rating','rating']); vehicle=col(df,['vehicle_id','model_id','ev_model_id'])
    if category:
        agg={}
        if sales: agg[sales]='sum'
        if price: agg[price]='mean'
        if rng: agg[rng]='mean'
        if rating: agg[rating]='mean'
        if vehicle: agg[vehicle]='nunique'
        if agg: df.groupby(category,dropna=False).agg(agg).to_csv(OUT/'category_summary.csv')
        else: df[category].value_counts(dropna=False).to_csv(OUT/'category_summary.csv')
        if sales: chart(df.groupby(category)[sales].sum().sort_values(ascending=False),'Annual EV Sales by Category','sales_by_category.png')
    if maker:
        agg={}
        if sales: agg[sales]='sum'
        if vehicle: agg[vehicle]='nunique'
        if price: agg[price]='mean'
        if agg: df.groupby(maker,dropna=False).agg(agg).to_csv(OUT/'manufacturer_summary.csv')
        else: df[maker].value_counts().to_csv(OUT/'manufacturer_summary.csv')
        if sales: chart(df.groupby(maker)[sales].sum().sort_values(ascending=False),'Top Manufacturers by Annual EV Sales','top_manufacturers.png',True,10)
    if region:
        df[region].value_counts(dropna=False).to_csv(OUT/'region_summary.csv'); chart(df[region].value_counts(),'Records by Region/Country','records_by_region.png',True)
    if battery:
        df[battery].value_counts(dropna=False).to_csv(OUT/'battery_summary.csv'); chart(df[battery].value_counts(),'Battery Technology Distribution','battery_distribution.png')
    if price:
        x=pd.to_numeric(df[price],errors='coerce').dropna()
        if len(x):
            fig,ax=plt.subplots(figsize=(9,5)); ax.hist(x,bins=30); ax.set_title('EV Price Distribution'); ax.set_xlabel(price); ax.set_ylabel('Records'); fig.tight_layout(); fig.savefig(CHARTS/'price_distribution.png',dpi=160); plt.close(fig)
    if rng and capacity:
        x=df[[rng,capacity]].apply(pd.to_numeric,errors='coerce').dropna()
        if len(x):
            fig,ax=plt.subplots(figsize=(8,5)); ax.scatter(x[capacity],x[rng],alpha=.25); ax.set_title('Battery Capacity vs Driving Range'); ax.set_xlabel(capacity); ax.set_ylabel(rng); fig.tight_layout(); fig.savefig(CHARTS/'battery_capacity_vs_range.png',dpi=160); plt.close(fig)
    print(f'Complete: {len(df):,} rows, {len(df.columns)} columns. Outputs saved to {OUT}')
if __name__=='__main__': main()
