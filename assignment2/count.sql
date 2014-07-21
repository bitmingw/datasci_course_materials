SELECT count(*) FROM (
    SELECT term
    FROM frequency
    WHERE term = "parliament"
) x;
