SELECT
    in_date,
    sh_name,
    (
        SELECT
            SUM(il_quantity * il_price)
        FROM
            invoice_line
        WHERE
            in_id = invoice.in_id
    ) AS total_cost
FROM
    invoice
    JOIN shipper USING(sh_id)
WHERE
    MONTH(in_date) = MONTH('$date-01')
    AND YEAR(in_date) = YEAR('$date-01')
ORDER BY
    in_date DESC