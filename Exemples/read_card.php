<?php
$servername = "localhost";
$username = "USER_NAME";
$password = "USER_PASSWORD";
$dbname = "USER_DATA_BASE_NAME";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "UPDATE `card_reader` SET valeur='Lire Carte...' WHERE id=1";
$sql2 = "UPDATE `card_reader` SET valeur='Lecture en cours...' WHERE id=2";
$sql3 = "UPDATE `card_reader` SET valeur='' WHERE id=3";
$sql4 = "UPDATE `card_reader` SET valeur='' WHERE id=4";
$sql5 = "UPDATE `card_reader` SET valeur='' WHERE id=5";
$sql6 = "UPDATE `card_reader` SET valeur='' WHERE id=6";
$sql7 = "UPDATE `card_reader` SET valeur='' WHERE id=7";
$sql8 = "UPDATE `card_reader` SET valeur='' WHERE id=8";

$conn->query($sql);
$conn->query($sql2);
$conn->query($sql3);
$conn->query($sql4);
$conn->query($sql5);
$conn->query($sql6);
$conn->query($sql7);
$conn->query($sql8);

$conn->close();
?>
