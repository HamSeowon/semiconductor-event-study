SELECT 
    p.date,
    p.daily_return AS stock_return,
    b.daily_return AS kospi_return,
    (p.daily_return - b.daily_return) AS excess_return
FROM daily_price p
JOIN benchmark_price b ON p.date = b.date
WHERE b.ticker = 'KOSPI'
ORDER BY p.date;