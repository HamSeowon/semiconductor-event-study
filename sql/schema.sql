CREATE TABLE IF NOT EXISTS daily_price (
    date TEXT,
    ticker TEXT,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume INTEGER,
    daily_return REAL,
    PRIMARY KEY (date, ticker)
);

CREATE TABLE IF NOT EXISTS benchmark_price (
    date TEXT,
    ticker TEXT,
    close REAL,
    daily_return REAL,
    PRIMARY KEY (date, ticker)
);

CREATE TABLE IF NOT EXISTS events (
    event_id TEXT PRIMARY KEY,
    ticker TEXT,
    event_date TEXT,
    event_description TEXT,
    event_type TEXT,
    expected_direction TEXT,
    anticipated TEXT,
    source TEXT
);
CREATE TABLE IF NOT EXISTS ticker_benchmark_map (
    ticker TEXT PRIMARY KEY,
    benchmark_ticker TEXT
);