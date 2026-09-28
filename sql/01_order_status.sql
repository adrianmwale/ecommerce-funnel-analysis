SELECT
    order_status,
    COUNT(*) AS orders,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM orders), 2) AS pct_of_total
FROM orders
GROUP BY order_status
ORDER BY orders DESC;