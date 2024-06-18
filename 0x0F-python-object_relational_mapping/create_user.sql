CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
DROP USER 'student'@'localhost';
SELECT User, Host FROM mysql.user;

ALTER USER 'student'@'localhost' IDENTIFIED BY 'student1234#';
ALTER USER 'learner'@'localhost' IDENTIFIED BY '';

CREATE USER IF NOT EXISTS 'student'@'localhost' IDENTIFIED BY 'student1234#';
GRANT ALL PRIVILEGES ON `hbtn_0e_0_usa`.* TO 'student'@'localhost';

GRANT ALL PRIVILEGES ON `hbtn_0e_0_usa`.* TO 'learner'@'localhost';

GRANT SELECT ON `performance_schema`.* TO 'learner'@'localhost';

GRANT SELECT ON `performance_schema`.* TO 'student'@'localhost';
FLUSH PRIVILEGES;
