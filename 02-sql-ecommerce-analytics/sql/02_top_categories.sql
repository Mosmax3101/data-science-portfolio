SELECT
    p.product_category_name AS category,
    COUNT(*) AS items_sold,
    ROUND(SUM(oi.price), 2) AS product_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN orders o ON oi.order_id = o.order_id
WHERE o.order_status = 'delivered'
GROUP BY category
ORDER BY product_revenue DESC
LIMIT 10;
