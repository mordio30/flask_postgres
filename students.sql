DROP TABLE IF EXISTS students;
CREATE TABLE students (
  id           serial PRIMARY KEY,
  first_name   varchar(255) NOT NULL,
  last_name    varchar(255) NOT NULL,
  age          integer NOT NULL,
  grade        varchar(2)
);


INSERT INTO students (id, first_name, last_name, age, grade) VALUES
    (1, 'John', 'Doe', 18, 'A'),
    (2, 'Jane', 'Smith', 19, 'B'),
    (3, 'Bob', 'Johnson', 20, 'C'),
    (4, 'Emily', 'Williams', 18, 'A'),
    (5, 'Michael', 'Brown', 19, 'B'),
    (6, 'Samantha', 'Davis', 22, 'A'),
    (7, 'Oliver', 'Jones', 20, 'B'),
    (8, 'Sophia', 'Miller', 21, 'A'),
    (9, 'Ethan', 'Wilson', 19, 'C'),
    (10, 'Isabella', 'Moore', 22, 'B');

