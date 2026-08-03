SELECT 
    p.date,
    p.ticker,
    p.daily_return AS stock_return,
    b.daily_return AS benchmark_return,
    m.benchmark_ticker,
    (p.daily_return - b.daily_return) AS excess_return
FROM daily_price p
JOIN ticker_benchmark_map m ON p.ticker = m.ticker
JOIN benchmark_price b ON p.date = b.date AND b.ticker = m.benchmark_ticker
ORDER BY p.ticker, p.date;
