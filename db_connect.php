<?php
// Database connection parameters
$servername = "localhost";
$username = "root"; // Default for phpMyAdmin
$password = ""; // Leave blank for default
$dbname = "ecommers";

// Create a connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>