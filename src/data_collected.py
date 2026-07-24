import FinanceDataReader as fdr
from pykrx import stock
import pandas as pd


START_DATE = "2026-01-01"
END_DATE = "2026-07-22"

STOCK_CODE = "000660" #sk hynix code

def collect_price_data():
    """SK하이닉스 일별 주가(OHLCV) 수집"""
    print("SK하이닉스 주가 데이터 수집 중...")
    df = fdr.DataReader(STOCK_CODE, START_DATE, END_DATE)
    df.to_csv("data/raw/sk_hynix_price.csv")
    print(f"완료: {len(df)}행 저장됨 -> data/raw/sk_hynix_price.csv")
    return df

def collect_kospi_data():
    """코스피 지수 수집 (비교 벤치마크)"""
    print("코스피 지수 데이터 수집 중...")
    df = fdr.DataReader("KS11", START_DATE, END_DATE)
    df.to_csv("data/raw/kospi.csv")
    print(f"완료: {len(df)}행 저장됨 -> data/raw/kospi.csv")
    return df

if __name__ == "__main__":
    price_df = collect_price_data()
    kospi_df = collect_kospi_data()

    print("\n=== 수집 결과 미리보기 ===")
    print("\n[주가]")
    print(price_df.head())
    print("\n[코스피]")
    print(kospi_df.head())
