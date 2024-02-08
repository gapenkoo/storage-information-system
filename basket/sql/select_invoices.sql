SELECT
    in_id,
    in_date,
    sh_name,
    status
FROM
    invoice
    JOIN shipper USING(sh_id)
WHERE
    status != 'APPROVED'