<?php
// Database connection details
$host = 'localhost';
$username = 'root';
$password = '';
$database = 'ecommerce';

// Connect to the database
$conn = new mysqli($host, $username, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get form data
$email = $_POST['email'];
$password = $_POST['password'];

// Check if the user exists
$sql_check = "SELECT * FROM users WHERE email = ?";
$stmt = $conn->prepare($sql_check);
$stmt->bind_param("s", $email);
$stmt->execute();
$result = $stmt->get_result();

if ($result->num_rows > 0) {
    $row = $result->fetch_assoc();
    // Verify the password
    if (password_verify($password, $row['password'])) {
        // Redirect to shop page after successful login
        header("Location: shop.html");
        exit(); // Ensure no further script execution
    } else {
        // Invalid password
        echo "<script>alert('Invalid password. Please try again.'); window.location.href='login.html';</script>";
    }
} else {
    // No account found with this email
    echo "<script>alert('No account found with this email. Please sign up first.'); window.location.href='signup.html';</script>";
}

// Close connection
$stmt->close();
$conn->close();
?>
