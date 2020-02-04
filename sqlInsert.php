<?php
$servername = "localhost";
$username = "erizho21";
$password = "zhou";
$dbname = "erizho21";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
// Insert Data
$sql = "INSERT INTO students (name, age, gradeLevel) VALUES ('Eric', '11', '16')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?> 
