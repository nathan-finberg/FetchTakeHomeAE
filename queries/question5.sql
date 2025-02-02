/* SPEND BY BRAND AMONG USERS CREATED LAST 6 MONTHS */

SELECT brand._id,
  brand.name,
  sum(receipt_item.price * receipt_item.quantity) AS spend
FROM receipt_item
JOIN brand
ON brand._id = receipt_item.brand_id
JOIN receipt
ON receipt._id = receipt_item.receipt_id
JOIN customer
ON customer._id = receipt.customer_id
WHERE customer.account_created_ts >= (now() - interval 6 month);
GROUP BY 1,2
ORDER BY 3 DESC
LIMIT 10;
