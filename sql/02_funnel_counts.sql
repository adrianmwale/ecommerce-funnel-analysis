SELECT
    COUNT(*) AS placed,
    COUNT(order_approved_at) AS approved,
    COUNT(order_delivered_carrier_date) AS shipped,
    COUNT(order_delivered_customer_date) AS delivered
FROM orders;