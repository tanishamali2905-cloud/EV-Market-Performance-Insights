from flask import Flask, render_template_string
app=Flask(__name__)
TABLEAU_URL='PASTE_YOUR_PUBLISHED_TABLEAU_URL_HERE'
PAGE='''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>EV Market Insights</title><style>body{font-family:Arial;margin:0;background:#f5f7f8}header{padding:20px 5%;background:#dff1df}main{padding:20px 5%}iframe{width:100%;height:780px;border:0}.notice{background:#fff4d6;padding:12px}</style></head><body><header><h1>EV Market Performance &amp; Insights</h1></header><main>{% if ready %}<iframe src="{{ url }}" title="Tableau dashboard"></iframe>{% else %}<p class="notice">Publish your Tableau view and replace TABLEAU_URL in app.py.</p>{% endif %}</main></body></html>'''
@app.route('/')
def index():
 ready=TABLEAU_URL.startswith('https://') and 'PASTE_YOUR' not in TABLEAU_URL
 return render_template_string(PAGE,ready=ready,url=TABLEAU_URL)
if __name__=='__main__': app.run(debug=True)
