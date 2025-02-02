/* ACCEPTED VS REJECTED AVERAGE SPEND */

/* OF NOTE: This relies on uniqueness of receipts which would be taken care of in loading the data */

SELECT reward_status, 
  average(total_spent) AS average_spend
FROM receipt
WHERE lower(reward_status) IN("accepted","rejected")
GROUP BY 1
ORDER BY 2 DESC;
