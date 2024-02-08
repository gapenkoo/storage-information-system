SELECT
    pr_name,
    pr_weight,
    pr_material,
    st_amount,
    st_price,
    st_date
FROM
    procurement
    JOIN store USING(pr_id)
WHERE
    pr_material LIKE '%$material%'