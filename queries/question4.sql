/* TOTAL ITEMS PURCHASED BY REWARD STATUS */

SELECT reward_status, 
  sum(purchased_item_count) AS total_item_count, 
  average(purchased_item_count) AS average_item_count
FROM receipt
WHERE lower(reward_status) IN("accepted", "rejected")
GROUP BY 1
ORDER BY 2 DESC;
