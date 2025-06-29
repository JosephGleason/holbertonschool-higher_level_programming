-- 1. Root user
-- Create user_0d_1@localhost with password user_0d_1_pwd if it doesn’t exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant ALL privileges on all databases and tables with grant option
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
