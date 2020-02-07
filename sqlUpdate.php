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
//Update Data
$sql = "UPDATE students SET gradeLevel='12' WHERE name='Eric' AND gradeLevel=11";

//Echos success or an error
if ($conn->query($sql) === TRUE) {
    echo "Record updated successfully";
} else {
    echo "Error updating record: " . $conn->error;
}

$conn->close();
?>
