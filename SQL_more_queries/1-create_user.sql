-- user_0d_1 istifadəçisini yaradın, əgər artıq varsa, səhv verməsin
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- user_0d_1 istifadəçisinə bütün server üzrə icazələr verin
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Dəyişiklikləri tətbiq edin
FLUSH PRIVILEGES;
