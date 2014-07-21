SELECT count(*) FROM (
    SELECT DISTINCT docid
    FROM frequency
    GROUP BY docid
    HAVING term = "transactions" AND term = "world"
) x;
