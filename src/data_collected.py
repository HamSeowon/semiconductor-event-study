import FinanceDataReader as fdr

START_DATE = "2026-01-01"
END_DATE = "2026-07-22"

#sk hynix stock price
def collect_price_data():
    df = fdr.DataReader("000660", START_DATE, END_DATE)
    df.to_csv("data/raw/sk_hynix_price.csv")
    return df

#KOSPI
def collect_kospi_data():
    df = fdr.DataReader("KS11", START_DATE, END_DATE)
    df.to_csv("data/raw/kospi.csv")
    return df

if __name__ == "__main__":
    price_df = collect_price_data()
    kospi_df = collect_kospi_data()

    print("\ Preview")
    print("\n Stock Price")
    print(price_df.head())
    print("\n KOSPI")
    print(kospi_df.head())
