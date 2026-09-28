WITH funnel AS (
    SELECT
        COUNT(*) AS placed,
        COUNT(order_approved_at) AS approved,
        COUNT(order_delivered_carrier_date) AS shipped,
        COUNT(order_delivered_customer_date) AS delivered
    FROM orders
)
SELECT
    placed,
    approved,
    ROUND(100.0 * approved / placed, 2) AS placed_to_approved_pct,
    shipped,
    ROUND(100.0 * shipped / approved, 2) AS approved_to_shipped_pct,
    delivered,
    ROUND(100.0 * delivered / shipped, 2) AS shipped_to_delivered_pct,
    ROUND(100.0 * delivered / placed, 2) AS overall_conversion_pct
FROM funnel;