import sqlite3
import pandas as pd

DB_PATH = "data/sk_hynix.db"

def create_tables(connection):
    with open("sql/schema.sql", "r") as f:
        schema = f.read()
    connection.executescript(schema)


def load_price_data(connection):
    df = pd.read_csv("data/processed/sk_hynix_price_clean.csv")
    df.columns = df.columns.str.lower()  
    df.rename(columns={"date": "date"}, inplace=True)
    df.to_sql("daily_price", connection, if_exists="replace", index=False)

def load_kospi_data(connection):
    df = pd.read_csv("data/processed/kospi_clean.csv")
    df.columns = df.columns.str.lower()
    df = df[["date", "close", "daily_return"]].copy()
    df["ticker"] = "KOSPI"
    df.to_sql("benchmark_price", connection, if_exists="replace", index=False)

def load_events_data(connection):
    df = pd.read_csv("data/raw/sk_hynix_event_log.csv")
    df.to_sql("events", connection, if_exists="replace", index=False)

if __name__ == "__main__":
    connection = sqlite3.connect(DB_PATH)
    create_tables(connection)
    load_price_data(connection)
    load_kospi_data(connection)
    load_events_data(connection)
    connection.close()