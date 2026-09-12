-- Storefronts being tracked, with the currency each one prices in.
CREATE TABLE IF NOT EXISTS stores (
    domain      TEXT PRIMARY KEY,
    name        TEXT NOT NULL,
    currency    TEXT NOT NULL,
    last_polled TEXT
);

-- Every product ever seen. first_seen_at identifies new drops.
CREATE TABLE IF NOT EXISTS products (
    store_domain  TEXT NOT NULL,
    product_id    INTEGER NOT NULL,
    handle        TEXT NOT NULL,
    title         TEXT NOT NULL,
    vendor        TEXT,
    product_type  TEXT,
    first_seen_at TEXT NOT NULL,
    PRIMARY KEY (store_domain, product_id)
);

-- Append-only log: one row per variant per poll. Rows are never updated,
-- since price drops are a comparison between consecutive observations.
CREATE TABLE IF NOT EXISTS observations (
    store_domain     TEXT    NOT NULL,
    product_id       INTEGER NOT NULL,
    variant_id       INTEGER NOT NULL,
    size             TEXT,
    price            REAL    NOT NULL,
    compare_at_price REAL,
    available        INTEGER NOT NULL,
    observed_at      TEXT    NOT NULL,
    PRIMARY KEY (variant_id, observed_at)
);

CREATE INDEX IF NOT EXISTS idx_obs_variant_time ON observations (variant_id, observed_at DESC);
CREATE INDEX IF NOT EXISTS idx_products_first_seen ON products (first_seen_at);
