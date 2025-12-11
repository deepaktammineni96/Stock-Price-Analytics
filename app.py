import os
import requests
from flask import Flask, request, jsonify, send_from_directory

# Flask app – Vercel expects an `app` object in this file
app = Flask(__name__, static_folder="static", static_url_path="")

FINNHUB_API_KEY = os.environ.get("FINNHUB_API_KEY")
FINNHUB_BASE_URL = "https://finnhub.io/api/v1/quote"


def fetch_quote(symbol: str) -> dict:
    """Call Finnhub quote endpoint for a single symbol."""
    params = {"symbol": symbol, "token": FINNHUB_API_KEY}
    try:
        resp = requests.get(FINNHUB_BASE_URL, params=params, timeout=5)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        return {"error": f"API error: {e}"}

    # Finnhub returns fields like: c (current price), d (change), dp (percent)
    if not isinstance(data, dict) or "c" not in data:
        return {"error": "No data"}

    return {
        "symbol": symbol,
        "price": data.get("c"),
        "change": data.get("d"),
        "change_percent": data.get("dp"),
        "open": data.get("o"),
        "high": data.get("h"),
        "low": data.get("l"),
        "previous_close": data.get("pc"),
    }


@app.route("/")
def index():
    """Serve the main HTML page."""
    return send_from_directory(app.static_folder, "index.html")


@app.route("/api/quotes")
def get_quotes():
    """Return quotes for comma-separated symbols.

    Example:
      GET /api/quotes?symbols=AAPL,MSFT,TSLA
    """
    if not FINNHUB_API_KEY:
        return jsonify({"error": "FINNHUB_API_KEY is not configured"}), 500

    symbols_param = request.args.get("symbols", "")
    symbols = [s.upper().strip() for s in symbols_param.split(",") if s.strip()]

    if not symbols:
        return jsonify({"error": "Missing symbols parameter"}), 400

    results = {}
    for symbol in symbols:
        results[symbol] = fetch_quote(symbol)

    return jsonify(results)


if __name__ == "__main__":
    # Local dev entrypoint
    app.run(debug=True)
