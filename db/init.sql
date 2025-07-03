
-- Create login info table
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) UNIQUE,
    password_hash VARCHAR(64)
);

-- Create saved ticker table        
CREATE TABLE saved_ticker (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    ticker VARCHAR(32),
    FOREIGN KEY (user_id) REFERENCES users(id)
);