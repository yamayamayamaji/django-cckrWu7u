CREATE DATABASE image_analysis;

CREATE USER 'webapp'@'%' IDENTIFIED BY 'mysql';

GRANT ALL PRIVILEGES ON *.* TO 'webapp'@'%';

FLUSH PRIVILEGES;
