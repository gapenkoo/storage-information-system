UPDATE
    external_users
SET
    name = '$name',
    city = '$city',
    sh_date = '$sh_date',
    sh_phone = '$sh_phone'
WHERE
    username = '$username'