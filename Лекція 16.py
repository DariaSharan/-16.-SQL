# Task 1
# 1. Write SQL queries for table creation for a data model that you created for prev homework (Airbnb model)

CREATE TABLE guest_rooms (
    guest_id serial PRIMARY KEY,
    guest_name VARCHAR(50) NOT NULL,
    number_of_people INT NOT NULL
);

CREATE TABLE host_rooms (
    host_id serial PRIMARY KEY,
    room_id INT NOT NULL,
    amount_of_residents INT NOT NULL,
    price DECIMAL(10,2),
    refrigerator VARCHAR(50) NOT NULL,
    A/C VARCHAR(50) NOT NULL,
    availability VARCHAR(50) NOT NULL
);

CREATE TABLE reservation (
    reservation_id serial PRIMARY KEY,
    room_id INT NOT NULL,
    guest_id INT NOT NULL,
    date_of_reservation DATE,
    price DECIMAL(10,2),
    date_of_check_in DATE,
    date_of_check_out DATE
);

CREATE TABLE reviews (
    review_id serial PRIMARY KEY,
    reservation_id INT NOT NULL,
    room_id INT NOT NULL,
    guest_id INT NOT NULL,
    date_of_review DATE,
    number_of_starts INT NOT NULL,
    text_of_review VARCHAR(50) NOT NULL

    FOREIGN KEY (reservation_id)
        REFERENCES reservation (reservation_id)
    FOREIGN KEY (room_id)
        REFERENCES host_rooms (room_id)
    FOREIGN KEY (guest_id)
        REFERENCES guest_rooms (guest_id)
)

# TAsk 2
# 2. Write 3 rows (using INSERT queries) for each table in the data model

INSERT INTO host_rooms (host_id, amount_of_residents, price, refrigerator, availability) VALUES (123, 2, 300, 'yes', 'yes'), (124, 10, 1000, 'yes', 'no'), (125, 5, 500, 'no', 'no');

INSERT INTO guest_rooms (guest_name, number_of_people) VALUES ('Joe Black', 1), ('Amanda Hudson', 5), ('Billi Bob', 2);

INSERT INTO reservation (room_id, guest_id, date_of_reservation, price, date_of_check_in, date_of_check_out) VALUES (123, 234, 12.02.2022, 1000, 17.02.2022, 20.02.2022), (124, 678, 12.07.2022, 200, 17.07.2022, 20.07.2022), (234, 123, 12.12.2022, 700, 17.12.2022, 20.12.2022);

INSERT INTO reviews (reservation_id, date_of_review, number_of_stars, text_of_review) VALUES (123, 12.02.2022, 4, 'I loved the place, however, the price was too high.'), (124, 21.07.2022, 3, 'Very dirty.'), (234, 22.12.2022, 4, 'Not bad but not good.')


# Task 3
# 3. Create the next analytic queries:
# 1. Find a user who had the biggest amount of reservations. Return user name and user_id

SELECT 
g.guest_id
,g.guest_name
FROM guest_rooms g
INNER JOIN (
    SELECT guest_id, COUNT(*) AS num_reservations
    FROM reservations
    GROUP BY guest_id
) r ON g.guest_id = r.guest_id
ORDER BY num_reservations DESC
LIMIT 1;