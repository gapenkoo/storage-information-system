SELECT
    sh_name,
    sh_city,
    sh_date,
    sh_phone
FROM
    shipper
WHERE
    sh_city LIKE '%$city%'