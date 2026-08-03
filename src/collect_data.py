import FinanceDataReader as fdr
import pandas as pd

START_DATE = "2025-01-01"
END_DATE = "2026-07-26"

#add/delete tickers
TICKERS = {
    "000660" : "sk_hynix",
    "005930" : "samsung_electronics",
    "MU" : "micron",
}

BENCHMARKS = {
    "KS11" : "KOSPI", #for korea tickers
    "IXIC" : "NASDAQ", #for micron
}

#stock prices @param stock ticker
def collect_price_data(ticker):
    df = fdr.DataReader(ticker, START_DATE, END_DATE)
    df["ticker"] = ticker
    df = df.reset_index()
    df = df.rename(columns={df.columns[0]: 'Date'})
    return df

def collect_all_prices():
    all_data = []
    for ticker in TICKERS:
        df = collect_price_data(ticker)
        df = df.rename(columns={df.columns[0]: 'Date'}) #
        all_data.append(df)
    combined = pd.concat(all_data,ignore_index = True)
    combined.to_csv("data/raw/multi_stock_price.csv", index = False)
    return combined

#BENCHMARK
def collect_all_benchmarks():
    all_data = []
    for code, name in BENCHMARKS.items():
        df = fdr.DataReader(code,START_DATE,END_DATE)
        df["ticker"] = name
        df = df.reset_index()
        df = df.rename(columns={df.columns[0]: 'Date'}) #
        all_data.append(df)
    combined = pd.concat(all_data,ignore_index = True)
    combined.to_csv("data/raw/benchmarks.csv",index=False)
    return combined

if __name__ == "__main__":
    price_df = collect_all_prices()
    bench_df = collect_all_benchmarks()
    print("\n - Preview 03 - ")
    print("\n Stock Price")
    print(price_df.groupby("ticker").size())
    print("\n Bench")
    print(bench_df.groupby("ticker").size())
    print(bench_df.head())
    