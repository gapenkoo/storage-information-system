-- Добавляем записи в таблицу shipper
INSERT INTO
    shipper (sh_id, sh_name, sh_city, sh_date, sh_phone)
VALUES
    (
        1,
        'Speedy Delivery',
        'New York',
        '2022-01-10',
        '212-555-1234'
    ),
    (
        2,
        'Quick Ship',
        'Los Angeles',
        '2022-01-11',
        '213-555-1234'
    ),
    (
        3,
        'Reliable Transports',
        'Chicago',
        '2022-01-12',
        '312-555-1234'
    ),
    (
        4,
        'Express Couriers',
        'Houston',
        '2022-01-13',
        '713-555-1234'
    ),
    (
        5,
        'Global Freight',
        'Phoenix',
        '2022-01-14',
        '602-555-1234'
    ),
    (
        6,
        'Punctual Logistics',
        'Philadelphia',
        '2022-01-15',
        '215-555-1234'
    ),
    (
        7,
        'Trusty Transporters',
        'San Antonio',
        '2022-01-16',
        '210-555-1234'
    ),
    (
        8,
        'Fast Forwarders',
        'San Diego',
        '2022-01-17',
        '619-555-1234'
    ),
    (
        9,
        'Swift Shipping',
        'Dallas',
        '2022-01-18',
        '214-555-1234'
    ),
    (
        10,
        'Move It Now',
        'San Jose',
        '2022-01-19',
        '408-555-1234'
    );

-- Добавляем записи в таблицу procurement
INSERT INTO
    procurement (pr_id, pr_name, pr_weight, pr_material)
VALUES
    (1, 'Metal Pipes', 100, 'Metal'),
    (2, 'Wooden Planks', 50, 'Wood'),
    (3, 'Plastic Sheets', 25, 'Plastic'),
    (4, 'Steel Beams', 200, 'Steel'),
    (5, 'Copper Wires', 30, 'Copper'),
    (6, 'Aluminum Foils', 10, 'Aluminum'),
    (7, 'Rubber Hoses', 40, 'Rubber'),
    (8, 'Glass Panes', 150, 'Glass'),
    (9, 'Ceramic Tiles', 60, 'Ceramic'),
    (10, 'Granite Blocks', 300, 'Granite');

-- Добавляем записи в таблицу invoice
INSERT INTO
    invoice (in_id, in_date, sh_id)
VALUES
    (1, '2022-02-10', 1),
    (2, '2022-02-11', 2),
    (3, '2022-02-12', 3),
    (4, '2022-02-13', 4),
    (5, '2022-02-14', 5),
    (6, '2022-02-15', 6),
    (7, '2022-02-16', 7),
    (8, '2022-02-17', 8),
    (9, '2022-02-18', 9),
    (10, '2022-02-19', 10);

-- Добавляем записи в таблицу invoice_line
INSERT INTO
    invoice_line (il_id, il_quantity, il_price, in_id, pr_id)
VALUES
    (1, 10, 100, 1, 1),
    (2, 15, 80, 2, 2),
    (3, 20, 60, 3, 3),
    (4, 5, 200, 4, 4),
    (5, 12, 150, 5, 5),
    (6, 25, 40, 6, 6),
    (7, 30, 30, 7, 7),
    (8, 18, 170, 8, 8),
    (9, 22, 110, 9, 9),
    (10, 16, 120, 10, 10);

-- Добавляем записи в таблицу store
INSERT INTO
    store (st_id, st_amount, st_price, st_date, pr_id)
VALUES
    (1, 100, 1000, '2022-03-10', 1),
    (2, 150, 1200, '2022-03-11', 2),
    (3, 200, 1100, '2022-03-12', 3),
    (4, 250, 1300, '2022-03-13', 4),
    (5, 300, 900, '2022-03-14', 5),
    (6, 350, 800, '2022-03-15', 6),
    (7, 400, 1400, '2022-03-16', 7),
    (8, 450, 1500, '2022-03-17', 8),
    (9, 500, 1600, '2022-03-18', 9),
    (10, 550, 1700, '2022-03-19', 10);

INSERT INTO
    `billet_delivery`.`users` (`username`, `password`, `role`)
VALUES
    ('director', '13032003', 'director');

INSERT INTO
    `billet_delivery`.`users` (`username`, `password`, `role`)
VALUES
    ('manager', '13032003', 'manager');

INSERT INTO
    `billet_delivery`.`users` (`username`, `password`, `role`)
VALUES
    ('logist', '13032003', 'logist');

INSERT INTO
    `billet_delivery`.`users` (`username`, `password`, `role`)
VALUES
    ('merchandiser', '13032003', 'merchandiser');