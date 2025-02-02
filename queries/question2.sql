/* TOP 5 BRANDS BY RECEIPTS SCANNED COMPARING LAST MONTH AND TWO MONTHS AGO 

OF NOTE: displaying this data could happen many ways, including running separate queries. as far as a single query
goes, unioning is cleaner than writing a super complex single query without the union for the sake of display.
*/

SELECT "TWO_MONTH" as timeframe,
brand._id,
brand.name,
count(distinct receipt._id) as unique_receipts
FROM receipt
JOIN receipt_item
ON receipt._id = receipt_item.receipt_id
JOIN brand
ON receipt_item.brand_id = brand._id
WHERE receipt.scanned_ts IS NOT NULL
AND month(date(receipt.scanned_ts)) = month(date(now())) - 2
GROUP BY 1,2,3
ORDER BY 4 DESC
LIMIT 5

UNION

SELECT "LAST_MONTH" as timeframe,
brand._id,
brand.name,
count(distinct receipt._id) as unique_receipts
FROM receipt
JOIN receipt_item
ON receipt._id = receipt_item.receipt_id
JOIN brand
ON receipt_item.brand_id = brand._id
WHERE receipt.scanned_ts IS NOT NULL
AND month(date(receipt.scanned_ts)) = month(date(now())) - 1
GROUP BY 1,2,3
ORDER BY 4 DESC
LIMIT 5;

