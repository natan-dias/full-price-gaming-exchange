[![codecov](https://codecov.io/gh/natan-dias/full-price-gaming-exchange/graph/badge.svg?token=2O9RE10XYN)](https://codecov.io/gh/natan-dias/full-price-gaming-exchange)

# Full Price Game Calculator

A funny currency converter that answers the real question: *how many full-price games is that worth?*

## Features

- Convert any price (BRL, USD or EUR) into Full Price Games (FPG)
- Fixed reference prices: **R$ 399**, **$ 70**, **€ 70**
- A verdict message telling you whether the purchase is game-worthy or not
- English and Portuguese language support

## How it works

Enter the price of anything — a hamburger, a coffee, a flight ticket — select the currency, and hit Convert. The result shows how many full-price games that item is worth, rounded to 2 decimal places.

**Example:** a R$ 20 hamburger = **0.05 FPG**. You're safe to buy it.

## Running locally - Python Backend

The repo includes a Python script that serves the app and exposes a `/calculate` API endpoint, useful for local development and testing.

```bash
python3 fpg.py
```

Then open [http://localhost:8000](http://localhost:8000).

To stop the server: `Ctrl + C`.

## GitHub Pages deployment

The live site uses only `index.html` — all calculation logic runs in JavaScript, so no server is needed. GitHub Pages serves static files for free, making it the simplest zero-config deployment option.

The Python script and its `/calculate` endpoint are kept in the repo for local testing, study and as a foundation for writing automated tests in the future.

To enable GitHub Pages: go to **Settings → Pages → Source**, select your main branch and root folder.
