/* BRAND WITH MOST TRANSACTIONS BY USERS WITH ACCOUNTS CREATED IN THE LAST 6 MONTHS */

SELECT brand._id,
brand.name,
count(distinct receipt._id) AS unique_transactions
FROM receipt
JOIN receipt_item
ON receipt._id = receipt_item.receipt_id
JOIN brand
ON receipt_item.brand_id = brand._id
JOIN customer
ON receipt.customer_id = customer._id
WHERE customer.account_created_ts >= (now() - interval 6 month)
GROUP BY 1,2
ORDER BY 3 DESC
LIMIT 10;
