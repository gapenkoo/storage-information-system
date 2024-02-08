SELECT
    sh_name,
    sh_city,
    sh_phone,
    pr_name,
    pr_material,
    il_quantity,
    il_price
FROM
    invoice
    JOIN invoice_line USING(in_id)
    JOIN shipper USING(sh_id)
    JOIN procurement USING(pr_id)
WHERE
    sh_name LIKE '%$name%'