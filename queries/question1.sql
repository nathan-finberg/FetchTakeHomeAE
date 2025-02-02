/* TOP 5 BRANDS BY RECEIPTS SCANNED LAST MONTH */

SELECT brand._id,
brand.name,
count(distinct receipt._id) as unique_receipts
FROM receipt
JOIN receipt_item
ON receipt._id = receipt_item.receipt_id
JOIN brand
ON receipt_item.brand_id = brand._id
WHERE receipt.scanned_ts IS NOT NULL
AND month(date(receipt.scanned_ts)) = month(date(now())) - 1
GROUP BY 1,2
ORDER BY 3 DESC
LIMIT 5;
