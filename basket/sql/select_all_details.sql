SELECT
    pr_id as code,
    pr_name,
    pr_weight,
    pr_material,
    st_amount,
    st_price as price
FROM
    billet_delivery.procurement
    JOIN store USING(pr_id)