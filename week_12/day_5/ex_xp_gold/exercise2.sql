-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

-- Exercise 2

--UPDATE students
--SET
--birth_date = '11-02-1998'
--WHERE
--last_name = 'Benichou'
--RETURNING
--last_name, birth_date

-- Update
--UPDATE students
--SET
--last_name = 'Guez'
--WHERE
--last_name = 'Grez'
--RETURNING
--first_name, last_name

--Delete

--DELETE FROM students
--WHERE first_name='Lea' AND last_name='Benichou'
--RETURNING *

-- Count

--SELECT count(*) FROM students;

--SELECT count(*)
--FROM students
--WHERE birth_date > '01-01-2000'

-- Insert/Alter
--q1
--ALTER TABLE students
--ADD COLUMN math_grade
--smallint

-- q2
--UPDATE students
--SET
--math_grade=80
--WHERE id='1'
--RETURNING *

-- q3
--UPDATE students
--SET
--math_grade = 90
--WHERE id IN ('2', '4')

-- q4
--UPDATE students
--SET
--math_grade = 40
--WHERE id = '6'
--RETURNING *

-- q5
--SELECT count(*)
--FROM students
--WHERE math_grade > 83

-- q6
--INSERT INTO students (first_name, last_name, birth_date, math_grade)
--VALUES
--('Omer', 'Simpson', '10-03-1980' ,70)

-- q7
--SELECT * FROM students


-- Bonus
--SELECT first_name, last_name, count(math_grade) AS total_grade
--FROM students
--GROUP BY last_name, first_name

-- Sum

SELECT sum(math_grade) AS sum_grades
FROM students


