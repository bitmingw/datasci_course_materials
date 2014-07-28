SELECT results FROM (
    SELECT a.row_num AS row_num, b.col_num AS col_num, SUM(a.value * b.value) AS results
    FROM a JOIN b ON a.col_num = b.row_num
    GROUP BY a.row_num, b.col_num
)
WHERE row_num = 2 AND col_num = 3;

