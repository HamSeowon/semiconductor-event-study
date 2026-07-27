import FinanceDataReader as fdr
import pandas as pd

START_DATE = "2026-01-01"
END_DATE = "2026-07-26"

#add/delete tickers
TICKERS = {
    "000660" : "sk_hynix",
    "005930" : "samsung_electronics"
}

#stock prices @param stock ticker
def collect_price_data(ticker):
    df = fdr.DataReader(ticker, START_DATE, END_DATE)
    df["ticker"] = ticker
    df = df.reset_index()
    return df

def collect_all_prices():
    all_data = []
    for ticker in TICKERS:
        df = collect_price_data(ticker)
        all_data.append(df)
    combined = pd.concat(all_data,ignore_index = True)
    combined.to_csv("data/raw/multi_stock_price.csv", index = False)
    return combined

#KOSPI
def collect_kospi_data():
    df = fdr.DataReader("KS11", START_DATE, END_DATE)
    df["ticker"] = "KOSPI"
    df = df.reset_index()
    df.to_csv("data/raw/kospi.csv",index=False)
    return df

if __name__ == "__main__":
    price_df = collect_all_prices()
    kospi_df = collect_kospi_data()

    print("\n Preview")
    print("\n Stock Price")
    print(price_df.head())
    print("\n KOSPI")
    print(kospi_df.head())
    print(price_df.groupby("ticker").size())
