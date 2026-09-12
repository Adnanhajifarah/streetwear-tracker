# streetwear-tracker

Tracks price drops and new releases across streetwear retailers by polling
their public Shopify catalogs and recording what it sees over time.

## Why

Stores tell you what something costs right now. They don't tell you that it
was $180 last Tuesday, or that it quietly appeared three days ago. That
history doesn't exist publicly, so this builds it: poll each store, append
every observation to SQLite, and derive the interesting parts from the log.

Two signals:

- **New drops** — a product seen for the first time
- **Price drops** — a variant cheaper than the last time it was observed

## Stores

| Store | Domain | Currency |
|---|---|---|
| Undefeated | undefeated.com | USD |
| Dover Street Market | shop.doverstreetmarket.com | GBP |
| Bodega | bdgastore.com | USD |

Currency is read from each store's `/cart.js` at poll time rather than
hardcoded. DSM prices in GBP and the catalog endpoint never says so.

## Data source

Shopify exposes a public `products.json` on every storefront. No API key, no
scraping, no bot-detection to work around. Checked `robots.txt` on each store
before including it; none restrict the path.

The tracker polls once daily and sends a `User-Agent` identifying itself.
These are small businesses paying for bandwidth.

## Setup

```bash
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
```

## Status

Work in progress.
