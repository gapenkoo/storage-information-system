SELECT
    pr_name,
    pr_weight,
    st_amount,
    st_price,
    MAX(st_date) as max
FROM
    procurement
    JOIN store USING(pr_id)
WHERE
    pr_name LIKE '%$name%'
GROUP BY
    pr_id,
    pr_material,
    st_date,
    pr_name,
    pr_weight,
    st_amount,
    st_price