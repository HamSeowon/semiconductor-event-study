SELECT 
    e.event_id,
    e.event_date,
    e.event_description,
    e.event_type,
    p.close AS price_on_event_day,
    LAG(p.close, 3) OVER (ORDER BY p.date) AS price_3days_before,
    LEAD(p.close, 3) OVER (ORDER BY p.date) AS price_3days_after
FROM events e
JOIN daily_price p ON e.event_date = p.date
ORDER BY e.event_date;