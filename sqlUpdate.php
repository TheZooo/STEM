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
// Update Data
$sql = "UPDATE students SET gradeLevel='12' WHERE id=2";

if ($conn->query($sql) === TRUE) {
    echo "Record updated successfully";
} else {
    echo "Error updating record: " . $conn->error;
}

$conn->close();
?>
