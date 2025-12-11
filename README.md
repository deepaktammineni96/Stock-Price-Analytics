# Stock Price Viewer (Flask + Vercel)

Simple demo app to fetch live stock prices from the Finnhub API and display them in a web UI.

## Stack

- Frontend: Static HTML + vanilla JavaScript (served from `static/index.html`)
- Backend: Flask app (`app.py`) deployed on Vercel
- Data Provider: Finnhub

## Project Structure

- `app.py` — Flask application, exposes:
  - `/` — serves `static/index.html`
  - `/api/quotes` — returns JSON quotes from Finnhub
- `static/index.html` — Front-end UI
- `requirements.txt` — Python dependencies

## Setup (Local)

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Export your Finnhub API key:

   ```bash
   export FINNHUB_API_KEY="your_key_here"
   ```

3. Run the app:

   ```bash
   python app.py
   ```

4. Open `http://127.0.0.1:5000/` in your browser.

## Deploying to Vercel

1. Push this folder as a Git repo (GitHub, GitLab, etc.).
2. In Vercel, create a new project and import the repo.
3. In the project settings, add an environment variable:

   - `FINNHUB_API_KEY` = your Finnhub API key

4. Deploy. The root URL will serve the UI, and `/api/quotes` will return data.

On the page, enter stock tickers like:

```text
AAPL, MSFT, TSLA
```

Click **Get Prices** or enable auto-refresh to see live updates.
