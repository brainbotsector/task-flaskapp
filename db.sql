CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    dob DATE NOT NULL,
    gender ENUM('Male','Female','Other'),
    phoneno VARCHAR(10),
    city VARCHAR(50),
    state VARCHAR(50),

    degree VARCHAR(50) NOT NULL,
    institution VARCHAR(100) NOT NULL,
    subject VARCHAR(50),
    cgpa DECIMAL(3,2),
    year_started YEAR,
    year_graduated YEAR
)