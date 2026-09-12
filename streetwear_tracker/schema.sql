-- Storefronts we poll. Currency is discovered per store, not assumed.
CREATE TABLE IF NOT EXISTS stores (
    domain      TEXT PRIMARY KEY,
    name        TEXT NOT NULL,
    currency    TEXT NOT NULL,
    last_polled TEXT
);

-- One row per product we have ever seen. first_seen_at is what makes
-- "new drop" answerable: a product whose first_seen_at is this run is new.
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

-- Append-only log: one row per variant per poll. Never updated, only
-- inserted. Price drops are a comparison between consecutive rows for
-- the same variant, so the history has to survive to be queryable.
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
