# Stock Price Viewer (Vercel + Python + HTML)

Simple demo app to fetch live stock prices from the Finnhub API and display them in a web UI.

## Stack

- Frontend: Static HTML + vanilla JavaScript
- Backend: Python (Flask) serverless function on Vercel
- Data Provider: [Finnhub](https://finnhub.io)

## Project Structure

- `index.html` — Frontend UI
- `api/quotes.py` — Python serverless function (mounted at `/api/quotes`)
- `requirements.txt` — Python dependencies for the Vercel Python runtime

## How to Use

1. Sign up at Finnhub and get an API key.
2. Create a new Git repo from this folder and push it to GitHub/GitLab/Bitbucket.
3. Create a new project on Vercel and import the repo.
4. In Vercel project settings, add an environment variable:

   - `FINNHUB_API_KEY` = your Finnhub API key

5. Deploy. After deployment, open the URL in a browser.

On the page, enter stock tickers like:

```text
AAPL, MSFT, TSLA
```

Click **Get Prices** or enable auto-refresh to see live updates.
