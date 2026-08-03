import sqlite3
import pandas as pd

DB_PATH = "data/tickers.db"

def normalize_ticker(value):
    ticker = str(value).strip()
    if ticker.isdigit():
        return ticker.zfill(6)
    return ticker.upper()

def create_tables(connection):
    with open("sql/schema.sql", "r") as f:
        schema = f.read()
    connection.executescript(schema)

def load_price_data(connection):
    df = pd.read_csv("data/processed/multi_stock_price_clean.csv", dtype={"ticker": str})
    df["ticker"] = df["ticker"].apply(normalize_ticker)
    df["date"] = pd.to_datetime(df["date"], format="mixed", errors="raise").dt.strftime("%Y-%m-%d")
    df.to_sql("daily_price", connection, if_exists="replace", index=False)
    print(f"price data: {len(df)} rows completed")

def load_benchmark_map(conn):
    mapping = pd.DataFrame({
        "ticker": ["000660", "005930", "MU"],
        "benchmark_ticker": ["KOSPI", "KOSPI", "NASDAQ"]
    })
    mapping["ticker"] = mapping["ticker"].apply(normalize_ticker)
    mapping.to_sql("ticker_benchmark_map", conn, if_exists="replace", index=False)
    print("load benchmark map completed")

def load_benchmark_data(conn):
    df = pd.read_csv("data/processed/bench_clean.csv", dtype={"ticker": str})
    df["ticker"] = df["ticker"].apply(normalize_ticker)
    df["date"] = pd.to_datetime(df["date"], format="mixed", errors="raise").dt.strftime("%Y-%m-%d")
    df = df[["date", "ticker", "close", "daily_return"]].copy()
    df.to_sql("benchmark_price", conn, if_exists="replace", index=False)
    print(f"benchmark: {len(df)} rows completed")

def load_events_data(connection):
    df = pd.read_csv("data/raw/event_log_full.csv", dtype={"ticker": str})
    df["ticker"] = df["ticker"].apply(normalize_ticker)
    parsed = pd.to_datetime(df["event_date"], format="mixed", errors="coerce")
    failed = df[parsed.isna()]
    if len(failed) > 0:
        print("failed to parce the date:", failed[["event_id", "event_date"]])
        raise ValueError(f"{len(failed)}rows need to be checked")
    df["event_date"] = parsed.dt.strftime("%Y-%m-%d")
    df.to_sql("events", connection, if_exists="replace", index=False)
    print(f"events: {len(df)} rows completed")

if __name__ == "__main__":
    connection = sqlite3.connect(DB_PATH)
    create_tables(connection)
    load_price_data(connection)
    load_benchmark_data(connection)
    load_benchmark_map(connection)
    load_events_data(connection)
    connection.close()
    print(f"\ncompleted")