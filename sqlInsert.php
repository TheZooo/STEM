<?php
$servername = "localhost";
$username = "user";
$password = "password";
$dbname = "school";

//Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
//Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
//Insert Data "name:Eric, age:16, gradeLevel:11"
$sql = "INSERT INTO students (name, age, gradeLevel) VALUES ('Eric', '16', '11')";

//Echos success or an error
if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?> 
