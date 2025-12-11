import os
import requests
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static", static_url_path="")

FINNHUB_API_KEY = os.environ.get("FINNHUB_API_KEY")
FINNHUB_BASE_URL = "https://finnhub.io/api/v1/quote"

def fetch_quote(symbol):
    params={"symbol":symbol,"token":FINNHUB_API_KEY}
    try:
        r=requests.get(FINNHUB_BASE_URL, params=params, timeout=5)
        r.raise_for_status()
        data=r.json()
    except Exception as e:
        return {"error":str(e)}
    if "c" not in data:
        return {"error":"No data"}
    return {
        "symbol":symbol,
        "price":data.get("c"),
        "change":data.get("d"),
        "change_percent":data.get("dp"),
        "open":data.get("o"),
        "high":data.get("h"),
        "low":data.get("l"),
        "previous_close":data.get("pc")
    }

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

@app.route("/api/quotes")
def quotes():
    if not FINNHUB_API_KEY:
        return jsonify({"error":"No FINNHUB_API_KEY"}),500
    sy=request.args.get("symbols","")
    symbols=[s.strip().upper() for s in sy.split(",") if s.strip()]
    if not symbols:
        return jsonify({"error":"Missing symbols"}),400
    return jsonify({s:fetch_quote(s) for s in symbols})

if __name__=="__main__":
    app.run(debug=True)
