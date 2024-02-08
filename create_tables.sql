CREATE TABLE shipper (
    sh_id INT PRIMARY KEY,
    sh_name VARCHAR(45),
    sh_city VARCHAR(45),
    sh_date DATE,
    sh_phone VARCHAR(45)
);

CREATE TABLE procurement (
    pr_id INT PRIMARY KEY,
    pr_name VARCHAR(45),
    pr_weight INT,
    pr_material VARCHAR(45)
);

CREATE TABLE invoice (
    in_id INT PRIMARY KEY,
    in_date DATE,
    sh_id INT,
    FOREIGN KEY (sh_id) REFERENCES shipper(sh_id)
);

CREATE TABLE invoice_line (
    il_id INT PRIMARY KEY,
    il_quantity INT,
    il_price INT,
    in_id INT,
    pr_id INT,
    FOREIGN KEY (in_id) REFERENCES invoice(in_id),
    FOREIGN KEY (pr_id) REFERENCES procurement(pr_id)
);

CREATE TABLE store (
    st_id INT PRIMARY KEY,
    st_amount INT,
    st_price INT,
    st_date DATE,
    pr_id INT,
    FOREIGN KEY (pr_id) REFERENCES procurement(pr_id)
);

CREATE TABLE `users` (
    `username` varchar(45) NOT NULL,
    `password` varchar(45) NOT NULL,
    `role` varchar(45) DEFAULT 'external',
    PRIMARY KEY (`username`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

CREATE TABLE `billet_delivery`.`reports_orders` (
    `rep_id` INT NOT NULL AUTO_INCREMENT,
    `rep_month` INT NOT NULL,
    `rep_year` INT NOT NULL,
    `in_id` INT NOT NULL,
    PRIMARY KEY (`rep_id`)
);