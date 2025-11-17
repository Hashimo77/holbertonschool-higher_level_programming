-- Yoxla, əgər user_0d_1 yoxdursa yaradılır
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
-- İcazələr ver (lazım gələrsə)
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Yoxla, əgər user_0d_2 yoxdursa yaradılır
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
-- İcazələr ver (lazım gələrsə)
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- İcazələri göstər
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
