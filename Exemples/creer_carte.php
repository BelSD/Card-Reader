<?php
error_reporting(E_ALL & ~E_NOTICE);
$servername = "localhost";
$username = "USER_NAME";
$password = "USER_PASSWORD";
$dbname = "USER_DATA_BASE_NAME";

$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
if ($_POST['envoie']=="yes")
{
    $sql = "UPDATE card_reader SET valeur='Creer Carte...' WHERE id=1";
    mysqli_query($conn, $sql);
    $sql = "UPDATE card_reader SET valeur='".date('d/m/Y')."' WHERE id=3";
    mysqli_query($conn, $sql);
    $sql = "UPDATE card_reader SET valeur='".$_POST['nom']."' WHERE id=4";
    mysqli_query($conn, $sql);
    $sql = "UPDATE card_reader SET valeur='".$_POST['prenom']."' WHERE id=5";
    mysqli_query($conn, $sql);
    $sql = "UPDATE card_reader SET valeur='".$_POST['nr_client']."' WHERE id=6";
    mysqli_query($conn, $sql);
    $sql = "UPDATE card_reader SET valeur='".$_POST['points']."' WHERE id=7";
    mysqli_query($conn, $sql);
    $sql = "UPDATE card_reader SET valeur='".date('d/m/Y')."' WHERE id=8";
    mysqli_query($conn, $sql);
    echo "<script type='text/javascript'>document.location.replace('index.php');</script>";
}
?>
<form action="" method="post">
  <p>Nom : <input type="text" id="nom" name="nom"></p>
  <p>Prénom : <input type="text" id="prenom" name="prenom"></p>
  <p>Nr. Client : <input type="text" id="nr_client" name="nr_client"></p>
  <p>Points : <input type="text" id="points" name="points"></p>
  <button type="submit" value="yes" id="envoie" name="envoie">Soumettre</button>
</form>
<?php
mysqli_close($conn);
?>