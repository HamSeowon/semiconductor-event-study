CREATE TABLE IF NOT EXISTS daily_price(
    date TEXT PRIMARY KEY,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume INTEGER,
    daily_return REAL
);

CREATE TABLE IF NOT EXISTS benchmark_price(
    date TEXT,
    ticker TEXT,
    close REAL,
    daily_return REAL,
    PRIMARY Key(date, ticker)
);

CREATE TABLE IF NOT EXISTS events(
    event_id TEXT PRIMARY KEY,
    event_date TEXT,
    event_name TEXT,
    even_type TEXT,
    expected_direction TEXT,
    anticipated TEXT,
    source TEXT
);