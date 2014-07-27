SELECT value FROM (
    SELECT A.row_num, B.col_num, SUM(A.value * B.value) AS value
    FROM a AS A
    JOIN b AS B
    ON A.col_num = B.row_num
    GROUP BY A.row_num, B.col_num
)
WHERE A.row_num = 2 AND B.col_num = 3;
