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
// Show Data
$sql = "SELECT * FROM students";
$result = $conn->query($sql);

$conn->close();
?> 
