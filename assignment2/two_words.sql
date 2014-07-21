SELECT count(*) FROM (
    SELECT docid as result1
    FROM frequency
    WHERE term = "transactions"
)
INNER JOIN
(
    SELECT docid as result2
    FROM frequency
    WHERE term = "world"
)
ON result1 = result2;
