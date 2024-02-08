SELECT
    rep_year,
    rep_month,
    sh_name,
    sh_city,
    pr_name,
    il_quantity as amount,
    il_price as price,
    in_date
FROM
    reports_orders
    JOIN invoice USING(in_id)
    JOIN invoice_line USING(in_id)
    JOIN shipper USING(sh_id)
    JOIN procurement USING(pr_id)
WHERE
    rep_month = MONTH('$date-01')
    AND rep_year = YEAR('$date-01');